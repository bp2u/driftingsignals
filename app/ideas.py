from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path

import bleach
import frontmatter
import markdown
from flask import current_app, url_for
from markupsafe import Markup
from werkzeug.utils import secure_filename

HUB_FILENAME = "idea.md"
RESERVED_PAGE_SLUGS = {"assets"}
MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "sane_lists", "nl2br", "toc"]
ALLOWED_TAGS = [
    "p",
    "a",
    "abbr",
    "b",
    "blockquote",
    "br",
    "code",
    "em",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "i",
    "img",
    "li",
    "ol",
    "pre",
    "span",
    "strong",
    "table",
    "tbody",
    "td",
    "th",
    "thead",
    "tr",
    "ul",
]
ALLOWED_ATTRS = {
    "a": ["href", "title", "rel"],
    "img": ["src", "alt", "title"],
    "th": ["align"],
    "td": ["align"],
    "h1": ["id"],
    "h2": ["id"],
    "h3": ["id"],
    "h4": ["id"],
    "h5": ["id"],
    "h6": ["id"],
    "code": ["class"],
    "pre": ["class"],
}

_RELATIVE_SRC = re.compile(
    r'(?P<attr>src|href)="(?P<url>(?:\./)?assets/[^"]+)"',
    re.IGNORECASE,
)


@dataclass(frozen=True)
class IdeaPage:
    slug: str
    title: str
    filename: str
    summary: str = ""
    order: int = 100


@dataclass(frozen=True)
class IdeaAsset:
    name: str
    relpath: str
    kind: str


@dataclass
class Idea:
    slug: str
    title: str
    summary: str
    date: date
    tags: list[str]
    status: str
    overview_html: Markup
    pages: list[IdeaPage] = field(default_factory=list)
    assets: list[IdeaAsset] = field(default_factory=list)
    source_dir: Path | None = None

    @property
    def is_draft(self) -> bool:
        return self.status.lower() in {"draft", "wip"}

    @property
    def document_count(self) -> int:
        return 1 + len(self.pages)

    @property
    def file_count(self) -> int:
        return self.document_count + len(self.assets)


@dataclass
class IdeaDocument:
    idea: Idea
    page: IdeaPage
    html: Markup


def content_dir() -> Path:
    return Path(current_app.config["CONTENT_DIR"])


def list_ideas() -> list[Idea]:
    ideas = [_load_idea(path) for path in _idea_dirs()]
    ideas = [idea for idea in ideas if idea is not None]
    ideas.sort(key=lambda idea: idea.date, reverse=True)
    return ideas


def get_idea(slug: str) -> Idea | None:
    safe = secure_filename(slug)
    if not safe or safe != slug:
        return None
    return _load_idea(content_dir() / safe)


def get_page(slug: str, page_slug: str) -> IdeaDocument | None:
    idea = get_idea(slug)
    if idea is None or page_slug in RESERVED_PAGE_SLUGS:
        return None
    page = next((item for item in idea.pages if item.slug == page_slug), None)
    if page is None or idea.source_dir is None:
        return None
    path = idea.source_dir / page.filename
    if not path.is_file():
        return None
    post = frontmatter.load(path)
    html = _render_markdown(_strip_leading_heading(post.content), idea.slug)
    return IdeaDocument(idea=idea, page=page, html=html)


def asset_path(slug: str, filename: str) -> Path | None:
    idea = get_idea(slug)
    if idea is None or idea.source_dir is None:
        return None
    assets_root = (idea.source_dir / "assets").resolve()
    if not assets_root.is_dir():
        return None
    candidate = (assets_root / filename).resolve()
    try:
        candidate.relative_to(assets_root)
    except ValueError:
        return None
    if not candidate.is_file():
        return None
    return candidate


def _idea_dirs() -> list[Path]:
    root = content_dir()
    if not root.is_dir():
        return []
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and (path / HUB_FILENAME).is_file()
    )


def _load_idea(path: Path) -> Idea | None:
    if current_app.debug:
        return _parse_idea(path)
    return _parse_idea_cached(path, _dir_fingerprint(path))


@lru_cache(maxsize=128)
def _parse_idea_cached(path: Path, _fingerprint: str) -> Idea | None:
    return _parse_idea(path)


def _dir_fingerprint(path: Path) -> str:
    if not path.is_dir():
        return ""
    parts: list[str] = []
    for item in sorted(path.rglob("*")):
        if item.is_file():
            stat = item.stat()
            parts.append(f"{item.relative_to(path)}:{stat.st_mtime_ns}:{stat.st_size}")
    return "|".join(parts)


def _parse_idea(path: Path) -> Idea | None:
    hub = path / HUB_FILENAME
    if not hub.is_file():
        return None
    post = frontmatter.load(hub)
    slug = path.name
    title = str(post.get("title") or _title_from_slug(slug))
    summary = str(post.get("summary") or _first_paragraph(post.content))
    tags = _as_str_list(post.get("tags"))
    status = str(post.get("status") or "published")
    overview = _render_markdown(post.content, slug)
    pages = _discover_pages(path)
    assets = _discover_assets(path)
    return Idea(
        slug=slug,
        title=title,
        summary=summary,
        date=_as_date(post.get("date")),
        tags=tags,
        status=status,
        overview_html=overview,
        pages=pages,
        assets=assets,
        source_dir=path,
    )


def _discover_pages(path: Path) -> list[IdeaPage]:
    pages: list[IdeaPage] = []
    for md_file in sorted(path.glob("*.md")):
        if md_file.name == HUB_FILENAME:
            continue
        post = frontmatter.load(md_file)
        slug = md_file.stem
        if slug in RESERVED_PAGE_SLUGS:
            continue
        title = str(post.get("title") or _heading_or_filename(post.content, slug))
        summary = str(post.get("summary") or _first_paragraph(post.content))
        order = post.get("order", 100)
        try:
            order = int(order)
        except (TypeError, ValueError):
            order = 100
        pages.append(
            IdeaPage(
                slug=slug,
                title=title,
                filename=md_file.name,
                summary=summary,
                order=order,
            )
        )
    pages.sort(key=lambda page: (page.order, page.title.lower()))
    return pages


def _discover_assets(path: Path) -> list[IdeaAsset]:
    assets_dir = path / "assets"
    if not assets_dir.is_dir():
        return []
    assets: list[IdeaAsset] = []
    for item in sorted(assets_dir.rglob("*")):
        if not item.is_file():
            continue
        relpath = item.relative_to(assets_dir).as_posix()
        suffix = item.suffix.lower()
        kind = "image" if suffix in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"} else "file"
        assets.append(IdeaAsset(name=item.name, relpath=relpath, kind=kind))
    return assets


def _render_markdown(source: str, idea_slug: str) -> Markup:
    raw = markdown.markdown(source, extensions=MARKDOWN_EXTENSIONS)
    rewritten = _rewrite_asset_urls(raw, idea_slug)
    cleaned = bleach.clean(
        rewritten,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        protocols=["http", "https", "mailto"],
        strip=True,
    )
    return Markup(cleaned)


def _rewrite_asset_urls(html: str, idea_slug: str) -> str:
    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        filename = url.split("assets/", 1)[1]
        href = url_for("main.idea_asset", slug=idea_slug, filename=filename)
        return f'{match.group("attr")}="{href}"'

    return _RELATIVE_SRC.sub(replace, html)


def _as_date(value) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str) and value.strip():
        return date.fromisoformat(value.strip()[:10])
    return date.today()


def _as_str_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    return [str(item).strip() for item in value if str(item).strip()]


def _title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def _strip_leading_heading(content: str) -> str:
    lines = content.splitlines()
    index = 0
    while index < len(lines) and not lines[index].strip():
        index += 1
    if index < len(lines) and lines[index].lstrip().startswith("# "):
        index += 1
        if index < len(lines) and not lines[index].strip():
            index += 1
        return "\n".join(lines[index:])
    return content


def _heading_or_filename(content: str, slug: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return _title_from_slug(slug)


def _first_paragraph(content: str) -> str:
    chunks = [chunk.strip() for chunk in content.split("\n\n") if chunk.strip()]
    for chunk in chunks:
        if chunk.startswith("#"):
            continue
        plain = re.sub(r"[*_`>#\[\]]", "", chunk)
        return " ".join(plain.split())[:220]
    return ""
