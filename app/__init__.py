
from flask import Flask
from flask_restx import Api
from werkzeug.exceptions import BadRequest

from app.api.rates.controller import rates_api as rates_ns
from app.utils.logger import logger
from app.utils.response import bad_request_response, error_response
from config import Config


def create_app():

    # Inititalize app
    app = Flask(__name__)

    # Add config
    app.config.from_object(Config)

    # Register error page
    register_error_pages(app)

    # Rest-X API namespaces
    api = Api(app, version=Config.SWAGGER_VERSION, title=Config.SWAGGER_TITLE, description=Config.SWAGGER_DESCRIPTION)
    api.add_namespace(rates_ns)

    return app


def register_error_pages(app):

    @app.errorhandler(BadRequest)
    def response_bad_request_wrapper(e):
        logger.error(e)
        return bad_request_response(reason=e)

    @app.errorhandler(Exception)
    def exception_wrapper(e):
        logger.error(e)
        return error_response(reason=e)
