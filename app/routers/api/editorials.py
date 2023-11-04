from flask import Blueprint

router = Blueprint("editorials", __name__, url_prefix="/editorials")


@router.route("/", methods=["GET"])
def get_editorials():
    return []
