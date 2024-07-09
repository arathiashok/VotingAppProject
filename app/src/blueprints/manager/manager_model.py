import mysql.connector
from typing import List, Dict
from src.config import db_config
import bcrypt
import mysql.connector
from src.config import db_config
from typing import Dict
from flask_login import UserMixin
from flask_mail import Message
from flask_mail import Mail
from flask import Flask
from flask import current_app

def get_manager_details() -> List[Dict]:

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE Role="Manager"')
    results = cursor.fetchone()
    cursor.close()
    connection.close()

    return results

def view_myprecinct() :
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_myprecinct')
    results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return results