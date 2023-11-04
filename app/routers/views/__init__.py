from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

#
from app.constants import TEMPLATES_DIR

router = Blueprint("views", __name__, template_folder=TEMPLATES_DIR)


@router.route("/", methods=["GET"])
def home():
    try:
        return render_template("/pages/index.html")
    except TemplateNotFound:
        abort(404)
