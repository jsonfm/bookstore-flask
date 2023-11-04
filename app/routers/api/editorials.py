from flask import Blueprint

# forms
from app.schemas.editorials.forms import CreateEditorialForm, UpdateEditorialForm

# services
from app.services.editorials import editorialsService

#
router = Blueprint("editorials", __name__, url_prefix="/editorials")


@router.route("/", methods=["GET"])
def get_editorials(limit: int = 30, offset: int = 30):
    items = editorialsService.get_items(limit, offset)
    return items


@router.route("/<editorial_id:int>", methods=["GET"])
def get_editorial(editorial_id: int):
    item = editorialsService.get_item(editorial_id)
    return item


@router.route("/", methods=["POST"])
def create_editorial(body: CreateEditorialForm):
    item = editorialsService.create(body.dict())
    return item


@router.route("/<editorial_id>", methods=["PUT"])
def update_editorial(editorial_id: int, body: UpdateEditorialForm):
    item = editorialsService.update(editorial_id, body.dict())
    return item
