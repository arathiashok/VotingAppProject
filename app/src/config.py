import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '3306',
    'database': 'voterdb',
    #'auth_plugin': 'mysql_native_password'
}



class Config:
    SECRET_KEY = os.urandom(32)
    DEBUG = True
    MAIL_DEFAULT_SENDER = "noreply@voterapp.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = 'voterapp5800@gmail.com'
    MAIL_PASSWORD = 'troc vwqv tasq lmtd'

