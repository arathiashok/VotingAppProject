import pytest
from flask import url_for
from src import create_app

import src.blueprints.main.main_routes as main_routes
from src.blueprints.manager import manager_routes
from src.blueprints.admin import admin_routes
from src.blueprints.voter import voter_routes
from flask_login import current_user, login_user
class TestMainRoute:
    def test_index_page(self):
        app = create_app().test_client()    
        assert b'VoteUSA' in app.get('/').data 

    def test_login_page_attributes(self):
        app = create_app().test_client()
        attributes = [b'email', b'password', b'Login', b'Submit']
        for attribute in attributes:
           assert attribute in app.get('/login').data

    def test_login_page_valid_voter_login(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        app = app.test_client()
        rv = app.post('/login', json={'email': 'voter@e', 'password':'oooooooo'})
        # Redirect
        assert rv.status_code == 302

    def test_login_page_invalid_voter_login(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        combinations = {
            'voter@ee': 'oooijasioaj', 
            '': 'asdfasdf',
            'voter@e': '', 
            '': ''
        }
        for usern, passw in combinations.items():
            appp = app.test_client()
            rv = appp.post('/login', json={'email': f'{usern}', 'password':f'{passw}'})
            # Redirect
            print(usern, rv.data)
            assert rv.status_code != 302

    #register page tests
    def test_register_page_attributes(self):
        app = create_app().test_client()
        attributes = [b'name1', b'name2', b'name3', b'age', b'address1', b'address2', b'city', b'state', b'zip', b'ID1', b'ID2', b'email', b'password']
        for attribute in attributes:
           assert attribute in app.get('/new').data

    #must reset database before running these tests, otherwise duplicate entry
    def test_register_page_valid_register(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        app = app.test_client()
        rv = app.post('/new', json={'name1': 'isabelle', 'name2': 'c', 'name3': 'paulsen', 'age':'21', 'address1':'115 n dubuque st', 'address2': 'apartment a', 'city': 'iowa city', 'state': 'ia', 'zip': '52246', "ID1":'id1', 'ID2': 'id2', 'email': 'ip@i', 'password': 'password', 'passwordConfirm': 'password'})
        # Redirect
        assert rv.status_code == 302
    
    def test_register_page_password_differ(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        app = app.test_client()
        rv = app.post('/new', json={'name1': 'isabelle', 'name2': 'c', 'name3': 'paulsen', 'age':'21', 'address1':'115 n dubuque st', 'address2': 'apartment a', 'city': 'iowa city', 'state': 'ia', 'zip': '52246', "ID1":'id1', 'ID2': 'id2', 'email': 'ip@a', 'password': 'password', 'passwordConfirm': 'notpassword'})
        # Redirect
        assert rv.status_code != 302

    def test_register_page_underage(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        app = app.test_client()
        rv = app.post('/new', json={'name1': 'isabelle', 'name2': 'c', 'name3': 'paulsen', 'age':'4', 'address1':'115 n dubuque st', 'address2': 'apartment a', 'city': 'iowa city', 'state': 'ia', 'zip': '52246', "ID1":'id1', 'ID2': 'id2', 'email': 'ip@b', 'password': 'password', 'passwordConfirm': 'password'})
        # Redirect
        assert rv.status_code != 302

    def test_register_page_zip(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        app = app.test_client()
        rv = app.post('/new', json={'name1': 'isabelle', 'name2': 'c', 'name3': 'paulsen', 'age':'21', 'address1':'115 n dubuque st', 'address2': 'apartment a', 'city': 'iowa city', 'state': 'ia', 'zip': '1', "ID1":'id1', 'ID2': 'id2', 'email': 'ip@c', 'password': 'password', 'passwordConfirm': 'password'})
        # Redirect
        assert rv.status_code != 302

    def test_register_page_state(self):
        app = create_app()
        app.config["WTF_CSRF_ENABLED"] = False
        app = app.test_client()
        rv = app.post('/new', json={'name1': 'isabelle', 'name2': 'c', 'name3': 'paulsen', 'age':'21', 'address1':'115 n dubuque st', 'address2': 'apartment a', 'city': 'iowa city', 'state': 'iowa', 'zip': '52246', "ID1":'id1', 'ID2': 'id2', 'email': 'ip@d', 'password': 'password', 'passwordConfirm': 'password'})
        # Redirect
        assert rv.status_code != 302

    def test_vote_first(self):
        #user hits "vote" for first time
        #it gives them form with candidates
        pass

    def test_vote_second(self):
        #user votes
        #user hits "vote" again
        #it doesn't let them vote again
        pass
    
    def test_candidate(self):
        #user clicks "learn more"
        #it gives them more candidate info
        pass

    def test_castVote(self):
        #user submits vote
        #it returns them to home screen
        pass 

    def test_ballot(self):
        #user logs in
        #they see list of elections that match zip
        pass

    
    
