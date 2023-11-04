from flask import Blueprint
from flask_pydantic import validate

from app.schemas.books.forms import CreateBookForm

router = Blueprint("books", __name__, url_prefix="/books")


@router.route("/", methods=["GET"])
def get_books():
    return "login"


@router.route("/<book_id>", methods=["GET"])
def get_book(book_id: str):
    return "book"


@router.route("/slug/<book_slug>", methods=["GET"])
def get_book_by_slug(book_slug: str):
    return "singup"


@router.route("/", methods=["POST"])
@validate()
def create_book(body: CreateBookForm):
    return "create book"


@router.route("/", methods=["PUT"])
def update_book():
    return "update book"


@router.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id: str):
    return "delete book"
