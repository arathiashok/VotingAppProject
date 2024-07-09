from flask import Blueprint

bp = Blueprint('manager_bp', __name__, template_folder = 'manager_templates')

from src.blueprints.manager import manager_routes