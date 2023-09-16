from flask import render_template
from flask import Blueprint
from flask import current_app

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    current_app.logger.debug("Entrei na Home")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/marcas")
def brands():
    return render_template("brands.html")
