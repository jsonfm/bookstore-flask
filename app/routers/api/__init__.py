from flask import Blueprint

#
from app.routers.api.auth import router as router_auth
from app.routers.api.books import router as router_books
from app.routers.api.editorials import router as router_editorials

router = Blueprint("books", __name__, url_prefix="/api/v1")

router.register_blueprint(router_auth)
router.register_blueprint(router_books)
router.register_blueprint(router_editorials)
