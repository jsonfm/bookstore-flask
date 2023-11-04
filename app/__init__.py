from flask import Flask

from app.routers.views import router as router_views


def get_app():
    app = Flask(__name__)
    app.register_blueprint(router_views)
    return app
