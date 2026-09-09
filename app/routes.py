from flask import (
    Blueprint,
    abort,
    current_app,
    render_template,
    send_from_directory,
)

from .ideas import asset_path, get_idea, get_page, list_ideas

bp = Blueprint("main", __name__)


@bp.app_context_processor
def inject_site():
    return {
        "site_name": current_app.config["SITE_NAME"],
        "site_tagline": current_app.config["SITE_TAGLINE"],
        "site_author": current_app.config["SITE_AUTHOR"],
        "site_author_url": current_app.config["SITE_AUTHOR_URL"],
    }


@bp.route("/")
def index():
    return render_template("index.html", ideas=list_ideas())


@bp.route("/ideas/<slug>/")
def idea_hub(slug: str):
    idea = get_idea(slug)
    if idea is None:
        abort(404)
    return render_template("idea.html", idea=idea)


@bp.route("/ideas/<slug>/<page>/")
def idea_page(slug: str, page: str):
    document = get_page(slug, page)
    if document is None:
        abort(404)
    return render_template("page.html", document=document, idea=document.idea)


@bp.route("/ideas/<slug>/assets/<path:filename>")
def idea_asset(slug: str, filename: str):
    path = asset_path(slug, filename)
    if path is None:
        abort(404)
    return send_from_directory(path.parent, path.name)
