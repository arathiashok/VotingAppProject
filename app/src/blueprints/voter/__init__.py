from flask import Blueprint

bp = Blueprint('voter_bp', __name__, template_folder = 'voter_templates')

from src.blueprints.voter import voter_routes