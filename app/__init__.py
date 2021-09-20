from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
   
    #initializing application
    app = Flask(__name__)

    #setting up configuaration
    app.config.from_object(config_options[config_name])

    #initializing Flask Extensions
    bootstrap.init_app(app)

    #registering blueprints
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    #setting up config
    from .request import config_request

    config_request(app)

    return app





