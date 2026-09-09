# Rebuild prompt: Drifting Signals

Use this prompt to rebuild the site from scratch.

## Goal

Build a Python Flask + Jinja blog-style site that displays AI ideas. Each idea is a hub (overview + related files). The site must expand by adding folders. It must run locally. Production source of truth is GitHub (`bp2u/driftingsignals`); Cloudflare is the intended host and should sync from that repo.

## Inputs

- Idea folders at `content/ideas/<slug>/`
- Published essays live as a hub `idea.md` with the full article and frontmatter
- Required hub file: `idea.md` with YAML frontmatter (`title`, `summary`, `date`, `tags`, `status`) and Markdown overview
- Extra Markdown files in the same folder become hub documents (`title`, `summary`, optional `order`)
- Files under `assets/` are downloadable attachments
- Environment: `SECRET_KEY`, `FLASK_DEBUG`, `HOST`, `PORT`, optional `CONTENT_DIR`, `SITE_NAME` (default: Drifting Signals), `SITE_TAGLINE` (default: I'm just trying to keep up.), `SITE_AUTHOR` (default: Brenden Portolese), `SITE_AUTHOR_URL` (LinkedIn)

## Outputs

- Home page of idea cards, newest first
- Byline “By Brenden Portolese” linking to LinkedIn on the home page, idea hubs, documents, and footer
- Idea hub page with overview, document list, and file list
- Rendered Markdown pages with rewritten `assets/` links
- Safe asset serving (no path traversal)
- 404 page
- Light and dark themes with a header toggle and `prefers-color-scheme` default
- `run.py` for PyCharm / local debug
- `wsgi.py` + gunicorn / Docker for a Python process
- `freeze.py` (Frozen-Flask) writing static files to `build/`
- `wrangler.jsonc` for Cloudflare Workers static assets: freeze, then upload `build/`
- GitHub repo `bp2u/driftingsignals` as the deploy source

## Dependencies

- Python 3.12
- Flask, Frozen-Flask, python-frontmatter, Markdown, bleach, gunicorn, python-dotenv

## Constraints

- Prefer Python. No CMS or database in v1.
- Do not require an admin UI; folders are the source of truth.
- Keep config out of code so the app can move to another host.
- Do not commit `.env`, `.venv`, or secrets. Ship `.env.example` only.
- Sanitize Markdown HTML. Serve assets only from each idea’s `assets/` directory.
- UI should be readable, mobile-friendly, and keyboard accessible (skip link, focus styles, theme button labels).
