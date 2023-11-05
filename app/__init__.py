from flask import Flask, jsonify

from app.config import config

#
from app.db import db

# routers
from app.routers.api import router as router_api_v1
from app.routers.views import router as router_views
from app.routers.views.admin import router as router_admin_views


def get_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URL

    app.register_blueprint(router_views)
    app.register_blueprint(router_admin_views)
    app.register_blueprint(router_api_v1)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
