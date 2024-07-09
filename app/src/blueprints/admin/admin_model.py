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
def get_test_table() -> List[Dict]:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE Role="Admin"')
    results = cursor.fetchone()
    cursor.close()
    connection.close()
    return results

def view_precinct():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_precinct')
    results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return results

def insert_precinct(Name, CandidateCount, street, state, zip, ZipStart, ZipEnd):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='insert_precinct', args=[Name, CandidateCount, street, state, zip, ZipStart, ZipEnd])
    connection.commit()
    cursor.close()
    connection.close()
    return True

def update_precinct(PID, Name, CandidateCount, zip, ZipStart, ZipEnd):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # if len(cursor.callproc(procname='get_precinct_info', args=[PID, Name]))==1:
    cursor.callproc(procname='update_precinct', args=[PID, Name, CandidateCount, zip, ZipStart, ZipEnd])
    connection.commit()
    cursor.close()
    connection.close()
    return True

def delete_precinct(PID, Name):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='del_precinct', args=[PID, Name])
    connection.commit()
    cursor.close()
    connection.close()
    return True

def view_races():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_races')
    results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return results

def insert_races(RName, term, CandidateCount, SDate, EDate):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='insert_races', args=[RName, term, CandidateCount, SDate, EDate])
    connection.commit()
    cursor.close()
    connection.close()
    return True


def update_races(RName, term, CandidateCount, SDate, EDate):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # if len(cursor.callproc(procname='get_precinct_info', args=[PID, Name]))==1:
    cursor.callproc(procname='update_races', args=[RName, term, CandidateCount, SDate, EDate])
    connection.commit()
    cursor.close()
    connection.close()
    return True

def delete_races(RName):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='del_races', args=[RName])
    connection.commit()
    cursor.close()
    connection.close()
    return True

def view_elections():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_elections')
    results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return results

def new_election(title, natural_geo, electoral_cons, public_status):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='new_election', args=[title, natural_geo, electoral_cons, public_status])
    # results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return True

def view_election(election_title):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_election', args=[election_title])
    results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return results

def update_election(old_title, new_title, natural_geography, electoral_con, public_status):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='update_election', args=[old_title, new_title, natural_geography, electoral_con, public_status])
    # results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return True

def delete_election(election_title):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='delete_election', args=[election_title])
    #results = [x.fetchall() for x in cursor.stored_results()][0]
    connection.commit()
    cursor.close()
    connection.close()
    return True

# Election Dates
def view_election_dates(election_title):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_election_date', args=[election_title])
    try:
        results = [x.fetchall() for x in cursor.stored_results()][0]
    except:
        results = []
    cursor.close()
    connection.close()
    return results

def delete_election_date(election_date_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='delete_election_date', args=[election_date_id])
    cursor.close()
    connection.commit()
    connection.close()
    return True

def update_election_date(election_date_id, election_title, start_date, end_date):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='update_election_date', args=[election_date_id, election_title, start_date, end_date])
    cursor.close()
    connection.commit()
    connection.close()
    return True

def new_election_date(election_title, start_date, end_date):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='new_election_date', args=[election_title, start_date, end_date])
    cursor.close()
    connection.commit()
    connection.close()
    return True

#Candidate
# Candidate 
def view_candidates(election_title):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='view_election_candidate', args=[election_title])
    try:
        results = [x.fetchall() for x in cursor.stored_results()][0]
    except:
        results = []
    cursor.close()
    connection.close()
    return results

def delete_candidate(candidate_id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='delete_election_candidate', args=[candidate_id])
    cursor.close()
    connection.commit()
    connection.close()
    return True

def update_candidate(candidate_id, election_title, electoral_race, candidate_fn, candidate_ln, info):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='update_election_candidate', args=[candidate_id, election_title, electoral_race, candidate_fn, candidate_ln, info])
    cursor.close()
    connection.commit()
    connection.close()
    return True

def new_candidate(election_title, electoral_race, candidate_fn, candidate_ln, info):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='new_election_candidate', args=[election_title, electoral_race, candidate_fn, candidate_ln, info])
    cursor.close()
    connection.commit()
    connection.close()
    return True


def approve_user(email):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='approve_user', args=[email])
    connection.commit()
    cursor.close()
    connection.close()
    with current_app.app_context():
        mail = Mail()
        msg = Message("Profile Request Approved", sender="noreply@voterapp.com", recipients=[email])
        msg.body = "Your voter profile request has been approved."
        mail.send(msg)
    return True
    
def deny_user(email):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='deny_user', args=[email])
    connection.commit()
    cursor.close()
    connection.close()
    app = Flask(__name__)
    with current_app.app_context(): 
        mail = Mail()
        msg = Message("Profile Request Denied", sender="noreply@voterapp.com", recipients=[email])
        msg.body = "Your voter profile request has been denied. Please contact administration if you believe this is a mistake."
        mail.send(msg)
    return True

def assign_Manager(ManagerID, PrecinctID, PrecinctName):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.callproc(procname='assign_manager', args=[ManagerID, PrecinctID, PrecinctName])
    connection.commit()
    cursor.close()
    connection.close()
    return True

if __name__ == '__main__':
    print('et@e')