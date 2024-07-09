import pytest
from flask import url_for
from src import create_app

import src.blueprints.main.main_routes as main_routes
from src.blueprints.manager import manager_routes
from src.blueprints.admin import admin_routes
from src.blueprints.voter import voter_routes
from flask_login import current_user, login_user

class TestManagerRoute():
    def test_manager_approve_user(self):
        #user with pending status
        #hit approve button
        #user with approved status
        pass

    def test_manager_deny_user(self):
        #user with pending status
        #hit approve button
        #user with denied status
        pass

    def test_manager_search_voter_redirect(self):
        #search voter database
        #redirects to /search
        pass

    def test_manager_search_voter_attributes(self):
        app = create_app().test_client()
        attributes = [b'name1', b'name2', b'name3', b'age', b'zip']
        for attribute in attributes:
            assert attribute in app.get('/').data

    #copy/paste these and switch to admin tests
