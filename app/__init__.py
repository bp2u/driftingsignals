import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def create_app() -> Flask:
    load_dotenv(_project_root() / ".env")

    app = Flask(__name__)
    content_dir = Path(
        os.environ.get("CONTENT_DIR", _project_root() / "content" / "ideas")
    )
    if not content_dir.is_absolute():
        content_dir = _project_root() / content_dir

    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev-only-change-me"),
        CONTENT_DIR=content_dir,
        SITE_NAME=os.environ.get("SITE_NAME", "Drifting Signals"),
        SITE_TAGLINE=os.environ.get(
            "SITE_TAGLINE", "Notes and experiments with language models"
        ),
    )

    from .routes import bp

    app.register_blueprint(bp)

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html"), 404

    return app
