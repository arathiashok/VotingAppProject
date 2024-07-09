from flask import Flask, request
from flask_bootstrap import Bootstrap5
import json
from src.config import Config
import flask.globals as flask_global
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import bcrypt
import src.blueprints.main.main_model as main_model
from src.blueprints.voter import bp as voter_bp
from src.blueprints.admin import bp as admin_bp
from src.blueprints.manager import bp as manager_bp
from src.blueprints.main import bp as main_bp
from flask_mail import Mail


def create_app(config_class = Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    #login_manager.login_view = 'login'
    # Initalize Flask Extentions
    bootstrap = Bootstrap5(app)
    mail = Mail(app)
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(voter_bp, url_prefix='/voter')
    app.register_blueprint(manager_bp, url_prefix='/manager')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    @login_manager.user_loader
    def user_loader(email):
        if email == '':
            return None
        users = main_model.get_user_auth(email)

        user = main_model.User(email)
        #user.name = users['name']
        user.status = users['status']
        user.zip = users['zip']

        return user
    return app


