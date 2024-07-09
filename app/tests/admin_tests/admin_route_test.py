import pytest
from flask import url_for
from src import create_app

import src.blueprints.main.main_routes as main_routes
from src.blueprints.manager import manager_routes
from src.blueprints.admin import admin_routes
from src.blueprints.voter import voter_routes
from flask_login import current_user, login_user
class TestAdminRoute:
    def test_elections(self):
        pass

    def test_update_candidate(self):
        pass

    def test_delete_candidate(self):
        pass

    def test_view_canddidate(self):
        pass

    def new_election_date(self):
        pass

    def update_election_date(self):
        pass

    def delete_election_date(self):
        pass

    def view_election_date(self):
        pass

