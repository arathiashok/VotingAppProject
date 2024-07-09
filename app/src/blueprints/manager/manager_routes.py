
from flask_login import login_required
import mysql.connector
from src.config import db_config
from src.blueprints.manager import bp
from flask import render_template
import src.blueprints.main.main_forms as main_forms
import src.blueprints.main.main_model as main_model
import urllib.parse
import src.blueprints.manager.manager_model as manager_model

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index() -> str:
    message = 'Logged in successfully !'
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    form = main_forms.SearchForm()
    return render_template('manager.html', message = message, data=data, form=form)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    form = main_forms.SearchForm()
    form2 = main_forms.LoginForm()
    name1 = form.name1.data
    name2 = form.name2.data
    name3 = form.name3.data
    #poll = form.poll.data
    zip = form.zip.data
    age = form.age.data
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    return render_template('managersearchresults.html', form=form2, name1 = name1, name2=name2, name3 = name3, zip=zip, age=age, data=data)

@bp.route('/manager_search_voters', methods=['GET', 'POST'])
@login_required
def manager_search_voters() -> str:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    form = main_forms.SearchForm()
    return render_template('manager_search_voters.html', data=data, form=form, encoder=urllib.parse)

@bp.route('/manager_view_precinct')
@login_required
def manager_view_precinct():
    precinct = manager_model.view_myprecinct()
    return render_template('ViewMyPrecinct.html', precincts = precinct)

# @bp.route('/manager_view_precinct')
# @login_required
# def manager_view_precinct() :
#     connection = mysql.connector.connect(**db_config)
#     cursor = connection.cursor()
#     cursor.execute('SELECT P.PrecinctID, P.PrecinctName, P.NumberofCandidates, P.State, P.ZipCode, P.ZipPlus4Start, p.ZipPlus4End FROM Precincts P join Users U ON P.PollingManagerID = U.User_ID;')
#     data = cursor.fetchall()
#     connection.commit()
#     cursor.close()
#     connection.close()
#     return data
