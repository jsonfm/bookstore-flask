from flask import Blueprint, abort, render_template

#
from app.constants import TEMPLATES_DIR

router = Blueprint(
    "admin_views", __name__, template_folder=TEMPLATES_DIR, url_prefix="/admin"
)


@router.route("/", methods=["GET"])
def home():
    return render_template("/pages/admin/index.html")


@router.route("/books", methods=["GET"])
def books():
    return render_template("/pages/admin/books/index.html")


@router.route("/books/create", methods=["GET"])
def create_book():
    return render_template("/pages/admin/books/create.html")


#
@router.route("/editorials", methods=["GET"])
def editorials():
    return render_template("/pages/admin/editorials/index.html")


@router.route("/editorials/create", methods=["GET"])
def create_editorial():
    return render_template("/pages/admin/editorials/create.html")
