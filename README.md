# Drifting Signals

A Flask site for publishing AI ideas. Each idea is a folder: an overview plus the notes and files that belong with it.

Source: [github.com/bp2u/driftingsignals](https://github.com/bp2u/driftingsignals). Cloudflare is the intended host — connect that repo in the dashboard so deploys follow `main`.

## Run locally (PyCharm or terminal)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

In PyCharm: set the project interpreter to `.venv`, then run `run.py`.

Copy `.env.example` to `.env` if you want to change the secret key, host, or port.

## Add an idea

Create `content/ideas/your-slug/idea.md`:

```markdown
---
title: Your idea
summary: One sentence.
date: 2026-09-07
tags: [ai]
status: published
---

Overview goes here.
```

Add more Markdown files in the same folder and attachments under `assets/`. Refresh the home page. In debug mode, new folders appear without a restart.

## Host (GitHub + Cloudflare Workers)

This is a Workers static-assets project, not a classic Pages output-directory site. `python freeze.py` writes HTML into `build/`. [wrangler.jsonc](wrangler.jsonc) tells Wrangler to run that freeze, then upload `build/`.

Push to [bp2u/driftingsignals](https://github.com/bp2u/driftingsignals). Cloudflare already installs `requirements.txt` and Python from `.python-version`. Leave the deploy command as `npx wrangler deploy` (production) / `npx wrangler versions upload` (other branches). If the dashboard Worker name is not `driftingsignals`, change `"name"` in `wrangler.jsonc` to match.

A good log shows `pip install`, then `Freezing site to .../build`, then Wrangler uploading assets. The previous failure (`Missing entry-point to Worker script or to assets directory`) meant Wrangler ran before any freeze and had nothing to publish.

Preview the static site locally:

```bash
python freeze.py
python -m http.server --directory build 8080
```

To run the Python process on another machine:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SECRET_KEY=a-long-random-value
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

Or build the image:

```bash
docker build -t drifting-signals .
docker run --rm -p 8000:8000 -e SECRET_KEY=a-long-random-value drifting-signals
```

## Theme

The site follows the system light/dark preference. Use the header button to override; the choice is stored in the browser.
