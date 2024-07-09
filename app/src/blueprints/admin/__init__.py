from flask import Blueprint

bp = Blueprint('admin_bp', __name__, template_folder = 'admin_templates')

from src.blueprints.admin import admin_routes