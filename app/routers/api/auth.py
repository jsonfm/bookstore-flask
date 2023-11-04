from flask import Blueprint
from flask_pydantic import validate

# foms
from app.schemas.auth.forms import LoginForm

# utils
from app.utils.auth import hash_password

router = Blueprint("auth", __name__, url_prefix="/auth")


@router.route("/login", methods=["POST"])
@validate()
def login(body: LoginForm):
    print("login: ", body.dict())
    return "login"


@router.route("/signup", methods=["POST"])
def signup():
    return "singup"
