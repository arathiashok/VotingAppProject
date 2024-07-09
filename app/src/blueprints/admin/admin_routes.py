
from src.blueprints.admin import bp, admin_model, admin_forms
from flask_login import login_required
from flask import Flask, render_template, request
from flask import render_template, redirect, url_for, request, session
import src.blueprints.admin.admin_forms as admin_forms
import src.blueprints.admin.admin_model as admin_model
import mysql.connector
from src.config import db_config
import src.blueprints.main.main_forms as main_forms
import src.blueprints.admin.admin_model as admin_model
import urllib.parse

@bp.route('/', methods=['GET'])
@login_required
def index() -> str:
    message = 'Logged in successfully !'
    form = main_forms.SearchForm()
    return render_template('admin.html', message = message, form=form)

@bp.route('/approve/<voter_id>', methods=['GET', 'POST'])
def approve_user(voter_id):
    admin_model.approve_user(urllib.parse.unquote(voter_id))
    return redirect(url_for('admin_bp.index'))

@bp.route('/deny/<voter_id>', methods=['GET','POST'])
def deny_user(voter_id):
    admin_model.deny_user(urllib.parse.unquote(voter_id))
    return redirect(url_for('admin_bp.index'))


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
    return render_template('adminsearchresults.html', form=form2, name1 = name1, name2=name2, name3 = name3, zip=zip, age=age, data=data)

@bp.route('/pending_voters', methods=['GET', 'POST'])
@login_required
def pending_voters() -> str:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    return render_template('pending_voters.html', data=data, encoder=urllib.parse)


@bp.route('/search_voters', methods=['GET', 'POST'])
@login_required
def search_voters() -> str:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    form = main_forms.SearchForm()
    return render_template('search_voters.html', data=data, form=form, encoder=urllib.parse)

@bp.route('/viewprecinct')
@login_required
def viewprecinct():
    precincts = admin_model.view_precinct()
    return render_template('ViewPrecinct.html', precincts = precincts)

@bp.route('/addprecinct', methods=['GET', 'POST'])
@login_required
def addprecinct():
    error = " "
    form = admin_forms.NewPrecinctForm()
    if form.validate_on_submit():
        admin_model.insert_precinct(form.PName.data, form.CandidateCount.data, form.Street.data, form.State.data, form.ZipCode.data, form.ZipStart.data, form.ZipEnd.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('AddPrecinct.html', form=form, error=error)

@bp.route('/editprecinct', methods=['GET', 'POST'])
@login_required
def editprecinct():
    error = " "
    form = admin_forms.UpdatePrecinctForm()
    if form.validate_on_submit():
        admin_model.update_precinct(form.PID.data, form.PName.data, form.CandidateCount.data, form.ZipCode.data, form.ZipStart.data, form.ZipEnd.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('EditPrecinct.html', form=form, error=error)

@bp.route('/delprecinct', methods=['GET', 'POST'])
@login_required
def delprecinct():
    error = " "
    form = admin_forms.DeletePrecinctForm()
    if form.validate_on_submit():
        admin_model.delete_precinct(form.PID.data, form.PName.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('DeletePrecinct.html', form=form, error=error)

@bp.route('/viewRaces')
@login_required
def viewraces():
    races = admin_model.view_races()
    return render_template('ViewRaces.html', races = races)

@bp.route('/addRaces', methods=['GET', 'POST'])
@login_required
def addraces():
    error = " "
    form = admin_forms.NewRaceForm()
    if form.validate_on_submit():
        admin_model.insert_races(form.RaceName.data, form.Term.data, form.NumofCandidates.data, form.StartDate.data, form.EndDate.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('AddRaces.html', form=form, error=error)

@bp.route('/editRaces', methods=['GET', 'POST'])
@login_required
def editraces():
    error = " "
    form = admin_forms.UpdateRaceForm()
    if form.validate_on_submit():
        admin_model.update_races(form.RaceName.data, form.Term.data, form.NumofCandidates.data, form.StartDate.data, form.EndDate.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('EditRaces.html', form=form, error=error)

@bp.route('/delRaces', methods=['GET', 'POST'])
@login_required
def delraces():
    error = " "
    form = admin_forms.DeleteRaceForm()
    if form.validate_on_submit():
        admin_model.delete_races(form.RaceName.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('DeleteRaces.html', form=form, error=error)

#Elections
@bp.route('/elections', methods=['GET'])
@login_required
def view_elections() -> str:
    elections = admin_model.view_elections()
    return render_template('elections.html', elections = elections)

@bp.route('/election/<election_title>', methods=['GET'])
@login_required
def view_election(election_title) -> str:
    election_data = admin_model.view_election(election_title)
    election_dates = admin_model.view_election_dates(election_title)
    election_candidates = admin_model.view_candidates(election_title)
    return render_template('view_election.html', election_title = election_title, election = election_data, dates = election_dates, candidates = election_candidates)


@bp.route('/election/new', methods=['GET', 'POST'])
@login_required
def new_election() -> str:
    error = ''
    form = admin_forms.ElectionForm()
    if form.validate_on_submit():
        try:
            admin_model.new_election(form.election_title.data, form.geography.data, form.electoral_constituency.data, form.public_status.data)
            return redirect(url_for('admin_bp.view_election', election_title=form.election_title.data))
        except:
            error = f'Issue adding this election. Try a different title or contact support.'
    return render_template('new_election.html', form = form, error = error)



@bp.route('/election/<election_title>/delete', methods=['GET', 'POST'])
@login_required
def delete_election(election_title) -> str:
    error = ''
    form = admin_forms.DeleteForm()
    if form.validate_on_submit():
        admin_model.delete_election(election_title)
        error = 'election deleted.'
        return redirect(url_for('admin_bp.view_elections'))
    return render_template('delete_election.html', value = election_title, item = 'Election', error=error, form = form)

        
@bp.route('/election/<election_title>/update', methods=['GET', 'POST'])
@login_required
def update_election(election_title) -> str:
    error = ''
    form = admin_forms.ElectionForm()
    data = admin_model.view_election(election_title)[0]
    form.election_title.data = data[0]
    form.geography.data = data[1]
    form.electoral_constituency.data = data[2]

    if form.validate_on_submit():
        admin_model.update_election(election_title, form.election_title.data, form.geography.data, form.electoral_constituency.data, form.public_status.data)
        return redirect(url_for('admin_bp.view_election', election_title=form.election_title.data))
    return render_template('update_election.html', election = election_title, form = form, election_title = election_title)

# Election Dates
@bp.route('election/<election_title>/date/<election_date_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_election_date(election_title, election_date_id):
        error = ''
        form = admin_forms.DeleteDateForm()
        if form.validate_on_submit():
            admin_model.delete_election_date(election_date_id)
            error = 'election date deleted.'
            return redirect(url_for('admin_bp.view_election', election_title = election_title))
        return render_template('delete_election.html', election_title = election_title, error=error, form = form, value = election_date_id, item='Election Date')

@bp.route('election/<election_title>/date/<election_date_id>/update', methods=['GET', 'POST'])
@login_required
def update_election_date(election_title, election_date_id):
    error = ''
    form = admin_forms.ElectionDateForm()
    if form.validate_on_submit():  
        admin_model.update_election_date(election_date_id=election_date_id,
                                         election_title=election_title, 
                                         start_date=form.start_date.data, 
                                         end_date=form.end_date.data)
        return redirect(url_for('admin_bp.view_election', election_title=election_title))
    return render_template('new_election_date.html', form=form)

@bp.route('election/<election_title>/date/new', methods=['GET', 'POST'])
@login_required
def new_election_date(election_title):
    error = ''
    form = admin_forms.ElectionDateForm()
    if form.validate_on_submit():  
        admin_model.new_election_date(election_title=election_title, 
                                      start_date=form.start_date.data, 
                                      end_date=form.end_date.data)
        return redirect(url_for('admin_bp.view_election', election_title=election_title))
    return render_template('new_election_date.html', form=form)

# Candidates
@bp.route('election/<election_title>/candidate/<candidate_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_candidate(election_title, candidate_id):
        error = ''
        form = admin_forms.DeleteCandidateForm()
        if form.validate_on_submit():
            admin_model.delete_candidate(candidate_id)
            error = 'election date deleted.'
            return redirect(url_for('admin_bp.view_election', election_title = election_title))
        return render_template('delete_election.html', election = election_title, error=error, form = form, item='Candidate', value=candidate_id)

@bp.route('election/<election_title>/candidate/<candidate_id>/update', methods=['GET', 'POST'])
@login_required
def update_candidate(election_title, candidate_id):
    error = ''
    form = admin_forms.CandidateForm()
    if form.validate_on_submit():  
        admin_model.update_candidate(candidate_id=candidate_id,
                                         election_title=election_title, 
                                         electoral_race=form.electoral_race.data,
                                         candidate_fn=form.candidate_fn.data, 
                                         candidate_ln=form.candidate_ln.data,
                                         info=form.info.data)
        return redirect(url_for('admin_bp.view_election', election_title=election_title))
    return render_template('new_election_date.html', form=form)

@bp.route('election/<election_title>/candidate/new', methods=['GET', 'POST'])
@login_required
def new_candidate(election_title):
    error = ''
    form = admin_forms.CandidateForm()
    if form.validate_on_submit():  
        admin_model.new_candidate(election_title=election_title, 
                                      electoral_race=form.electoral_race.data,
                                      candidate_fn=form.candidate_fn.data, 
                                      candidate_ln=form.candidate_ln.data,
                                      info = form.info.data)
        return redirect(url_for('admin_bp.view_election', election_title=election_title))
    return render_template('new_election_candidate.html', form=form)

@bp.route('/assignManager', methods=['GET', 'POST'])
@login_required
def assign_Manager():
    error = " "
    form = admin_forms.AddManager()
    if form.validate_on_submit():
        admin_model.assign_Manager(form.ManagerID.data, form.PrecinctID.data, form.PrecinctName.data)
        return redirect(url_for('admin_bp.index'))
    return render_template('AssignManager.html', form=form, error=error)
