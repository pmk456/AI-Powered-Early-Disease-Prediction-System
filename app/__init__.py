from flask import Flask
from app.routes import routes
def create_app():
    app_ = Flask(__name__)
    app_.register_blueprint(routes)
    return app_