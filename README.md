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

## Host (GitHub + Cloudflare Pages)

`python freeze.py` renders the Flask site into `build/` (gitignored). Cloudflare Pages serves that folder.

Push to `main` on [bp2u/driftingsignals](https://github.com/bp2u/driftingsignals). In the Cloudflare project, set:

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Build command | `python freeze.py` |
| Build output directory | `build` |

Pages already installs `requirements.txt` and reads `.python-version`. After a push, the build log should show Python install, `pip install`, then `Freezing site to .../build`.

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
