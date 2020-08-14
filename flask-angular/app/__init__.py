import os
from flask import Flask, make_response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    db.create_all()
    db.session.commit()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,
                static_folder='./http/web-app/dist/web-app/',
                static_url_path="/")

    # Enable CORS
    CORS(app)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI= 'sqlite:///' + os.path.join(app.instance_path, 'pm-dev.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile(
    #         'config.py',
    #         silent=True
    #     )
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import models
    db.init_app(app)

    @app.route("/")
    def index():
        return make_response(open('app/http/web-app/dist/web-app/index.html').read())

    # Create App Blueprints
    from app.api import resource
    from app.api import categories
    app.register_blueprint(resource.resource_bp, url_prefix="/api")
    app.register_blueprint(categories.categories_bp, url_prefix="/api")

    return app