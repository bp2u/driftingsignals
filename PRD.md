# Drifting Signals — PRD

## Purpose

A blog-style site for publishing AI ideas. Each idea is a hub with an overview and related files. The site must grow by adding folders, not by changing application code.

## Audience

The author first, then anyone who visits once the app is hosted on another machine.

## Content model

An idea lives at `content/ideas/<slug>/`.

| File | Role |
| --- | --- |
| `idea.md` | Required hub. YAML frontmatter plus overview Markdown. |
| `*.md` | Extra documents listed on the hub and rendered at `/ideas/<slug>/<page>/`. |
| `assets/*` | Images, CSVs, and other files served from `/ideas/<slug>/assets/<file>`. |

Frontmatter on `idea.md`:

- `title` (string)
- `summary` (string)
- `date` (ISO date)
- `tags` (list)
- `status` (`published` or `draft`)

Other Markdown files may set `title`, `summary`, and optional `order` (integer). If they do not, the first heading and first paragraph are used, and documents sort by title. Quote YAML summaries that contain colons.

## Routes

- `/` — idea cards, newest first
- `/ideas/<slug>/` — hub
- `/ideas/<slug>/<page>/` — extra document
- `/ideas/<slug>/assets/<path>` — attachment (only files under that idea’s `assets/` folder)

## Authoring

Drop a new folder under `content/ideas/` and refresh. In debug mode the folder is read on each request. Production caches by file fingerprint until the process restarts or files change.

An admin UI is deferred. When it is added, it should write this same folder format.

## Hosting

Source of truth is the GitHub repo [bp2u/driftingsignals](https://github.com/bp2u/driftingsignals). Cloudflare is the intended production host: connect that repo so pushes to `main` deploy.

The app is a Flask process. Configure `SECRET_KEY`, `HOST`, and `PORT` through the environment. Run locally with `python run.py`. Run a Python process with `gunicorn --bind 0.0.0.0:8000 wsgi:app` or the included Dockerfile. Cloudflare Pages will not execute Flask unless the project uses a worker/container or a static export.

## Appearance

Editorial reading layout. Cards on the home page. Light and dark themes, following the system preference until the visitor toggles. The choice is stored in `localStorage`.

## Out of scope (v1)

- Admin create/edit UI
- Accounts, comments, search, or a database
- Real idea content (placeholders until the three ideas are collected)

## Success

A visitor can open the home page, enter an idea hub, read a related document, open an attachment, and switch themes. Adding a fourth folder appears on the home page without a code change.
