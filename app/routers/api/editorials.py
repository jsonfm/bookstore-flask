from flask import Blueprint
from flask_pydantic import validate

# forms
from app.schemas.editorials.forms import CreateEditorialForm, UpdateEditorialForm

# services
from app.services.editorials import editorialsService

#
router = Blueprint("editorials", __name__, url_prefix="/editorials")


@router.route("/", methods=["GET"])
def get_editorials(limit: int = 30, offset: int = 0):
    try:
        items = editorialsService.get_items(limit, offset)
        return items
    except Exception as e:
        return "error"


@router.route("/<int:editorial_id>", methods=["GET"])
def get_editorial(editorial_id: int):
    item = editorialsService.get_item(editorial_id)
    return item


@router.route("/", methods=["POST"])
@validate()
def create_editorial(body: CreateEditorialForm):
    item = editorialsService.create(body.dict())
    return item


@router.route("/<editorial_id>", methods=["PUT"])
@validate()
def update_editorial(editorial_id: int, body: UpdateEditorialForm):
    item = editorialsService.update(editorial_id, body.dict())
    return item
