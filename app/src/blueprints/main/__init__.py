from flask import Blueprint

bp = Blueprint('main_bp', __name__, template_folder = 'main_templates')

from src.blueprints.main import main_routes