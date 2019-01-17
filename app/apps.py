"""
 App module to bring together the whole app.

"""

# Standard library import
import os
from datetime import timedelta

# Third party imports
from flask import Flask
from flask_jwt_extended import JWTManager

# Local imports
from .api.v2.db_config import create_tables, drop_all
from instance.config import app_config
from .api.v2.db_config import conn

jwt =JWTManager()
secret_key = os.getenv('SECRET')

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False 

    create_tables()
    app.config['JWT_SECRET_KEY'] = secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=72)
    cur = conn.cursor()
    from .api.v2.routes import version2 as v_2
    app.register_blueprint(v_2)

    return app