from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

#
from app.constants import TEMPLATES_DIR

router = Blueprint("views", __name__, template_folder=TEMPLATES_DIR)


@router.route("/", methods=["GET"])
def home():
    return render_template("/pages/index.html")


@router.route("/about", methods=["GET"])
def about():
    return render_template("/pages/about.html")


@router.route("/contact", methods=["GET"])
def contact():
    return render_template("/pages/contact.html")


@router.route("/login", methods=["GET"])
def login():
    return render_template("/pages/login/index.html")


@router.route("/explore", methods=["GET"])
def explore():
    return render_template("/pages/explore.html")
