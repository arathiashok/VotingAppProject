import bcrypt
import pytest
import src.blueprints.main.main_model as main_model

class TestMainModel:
    def test_get_valid_user_auth(self):
        test_email = 'voter@e'
        assert main_model.get_user_auth(test_email)['email'] == test_email
        assert main_model.get_user_auth(test_email)['user_id'] == 1

    def test_get_invalid_user_auth(self):
        test_email = 'whoisthis@gmail.com'
        assert main_model.get_user_auth(test_email) == dict()

    def test_hash_password(self):
        password = 'mypasswd'
        salt = bcrypt.gensalt()
        assert main_model.hash_password(password, salt.decode('utf-8')) == bcrypt.hashpw(password.encode('utf-8'), salt)

    def test_insert_vote(self):
        #user votes
        #test if vote appears in Votes table
        pass

    def test_get_vote(self):
        #user votes
        #test if vote is gotten from Votes table
        pass

    def test_update_votes(self):
        #user votes
        #test if candidate votes increase by 1
        pass