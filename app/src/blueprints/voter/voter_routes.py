
from flask_login import login_required
import mysql.connector
from src.config import db_config
from src.blueprints.voter import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index() -> str:
    message = 'Logged in successfully !'
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM Elections")
    cursor.execute("SELECT DISTINCT E.* FROM Elections E join Precincts P ON E.ElectoralConstituency=P.ZipCode join Users U ON P.ZipCode=U.Zipcode")
    elections = cursor.fetchall()
    return render_template('voter.html', message = message, elections = elections)

@bp.route('/summary', methods=['GET', 'POST'])
@login_required
def summary() -> str:
    message = 'Summary of votes made for current Active Elections!'
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT C.ElectoralRace as ElectoralRace, CONCAT(C.CandidateFirstName,' ',C.CandidateLastName) AS CandidateName FROM ElectionCandidates C join Elections E ON C.ElectionTitle = E.ElectionTitle join Precincts P ON E.ElectoralConstituency=P.ZipCode join Users U ON P.ZipCode=U.Zipcode where C.CandidateVotes = (select max(EC.CandidateVotes) from ElectionCandidates EC group by EC.ElectoralRace)")
    summary = cursor.fetchall()
    return render_template('Summary.html', message = message, Summary = summary)
