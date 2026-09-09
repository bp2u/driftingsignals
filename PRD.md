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

Source of truth is the GitHub repo [bp2u/driftingsignals](https://github.com/bp2u/driftingsignals). Cloudflare Workers (static assets) is the production host: connect that repo so pushes to `main` deploy.

Workers cannot run Flask. `freeze.py` writes static files into `build/`. [wrangler.jsonc](wrangler.jsonc) runs that freeze, then uploads `build/` as assets (`not_found_handling`: `404-page`).

Authoring locally still uses `python run.py`. A Python process can run with `gunicorn --bind 0.0.0.0:8000 wsgi:app` or the included Dockerfile. Configure `SECRET_KEY`, `HOST`, and `PORT` through the environment when a server is used.

## Appearance

Editorial reading layout. Cards on the home page. Tagline: “I'm just trying to keep up.” Home heading: “Musings and mutterings on stuff that is distracting me from real life.” Byline “By Brenden Portolese” links to https://www.linkedin.com/in/brendenportolese/ on the home page, idea pages, and footer. Light and dark themes, following the system preference until the visitor toggles. The choice is stored in `localStorage`.

## Out of scope (v1)

- Admin create/edit UI
- Accounts, comments, search, or a database
- A CMS: published essays are added as folders, not through an editor

## Success

A visitor can open the home page, enter an idea hub, read a related document, open an attachment, and switch themes. Adding another folder appears on the home page without a code change.
