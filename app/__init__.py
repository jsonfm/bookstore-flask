from flask import Flask

from app.routers.api import router as router_api_v1
from app.routers.views import router as router_views
from app.routers.views.admin import router as router_admin_views


def get_app():
    app = Flask(__name__)
    app.register_blueprint(router_views)
    app.register_blueprint(router_admin_views)
    app.register_blueprint(router_api_v1)
    return app
