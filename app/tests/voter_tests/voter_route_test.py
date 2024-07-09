import pytest
from flask import url_for
from src import create_app

import src.blueprints.main.main_routes as main_routes
from src.blueprints.manager import manager_routes
from src.blueprints.admin import admin_routes
from src.blueprints.voter import voter_routes
from flask_login import current_user, login_user

class TestVoterRoute():
    def test_voter_homepage_pending(self):
        #pending voter
        #hompage tells them they're pending
        pass

    def test_voter_homepage_denied(self):
        #denied voter
        #homepage tells them they're denied
        pass

    def test_voter_homepage_approved(self):
        #approved voter
        #homepage tells them they are approved
        pass
