from flask import Blueprint

from app.utils.auth import hash_password

router = Blueprint("auth", __name__, url_prefix="/auth")


@router.route("/login", methods=["POST"])
def login():
    return "login"


@router.route("/signup", methods=["POST"])
def signup():
    return "singup"
