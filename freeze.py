"""Render the Flask site to static files for Cloudflare Pages."""

from pathlib import Path

from flask import url_for
from flask_frozen import Freezer

from app import create_app
from app.ideas import list_ideas

PROJECT_ROOT = Path(__file__).resolve().parent
BUILD_DIR = PROJECT_ROOT / "build"


def create_freezer():
    app = create_app()
    app.config.update(
        FREEZER_DESTINATION=str(BUILD_DIR),
        FREEZER_REMOVE_EXTRA_FILES=True,
    )
    freezer = Freezer(app)

    @freezer.register_generator
    def iter_content_urls():
        yield url_for("main.index")
        for idea in list_ideas():
            yield url_for("main.idea_hub", slug=idea.slug)
            for page in idea.pages:
                yield url_for("main.idea_page", slug=idea.slug, page=page.slug)
            for asset in idea.assets:
                yield url_for(
                    "main.idea_asset", slug=idea.slug, filename=asset.relpath
                )

    return app, freezer


def write_pages_files(app, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    with app.test_client() as client:
        response = client.get("/missing-for-static-404/")
    (dest / "404.html").write_bytes(response.data)
    (dest / "_redirects").write_text(
        "/ideas/:slug /ideas/:slug/ 308\n"
        "/ideas/:slug/:page /ideas/:slug/:page/ 308\n",
        encoding="utf-8",
    )


def main() -> None:
    app, freezer = create_freezer()
    print(f"Freezing site to {BUILD_DIR}")
    freezer.freeze()
    write_pages_files(app, BUILD_DIR)
    print("Done.")


if __name__ == "__main__":
    main()
