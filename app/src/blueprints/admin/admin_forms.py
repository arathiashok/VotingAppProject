from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, EmailField, PasswordField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
import secrets 


class NewPrecinctForm(FlaskForm):
    PName = StringField("Precinct Name", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Precinct Name"})
    CandidateCount = IntegerField("Candidates Count", validators=[DataRequired()], render_kw={"placeholder": "NumofCandidates"})
    Street = StringField("Street", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Street"})
    State = StringField("State", validators=[DataRequired(), Length(1, 2)], render_kw={"placeholder": "State"})
    ZipCode = IntegerField("ZipCode", validators=[DataRequired()], render_kw={"placeholder": "ZipCode"})
    ZipStart = IntegerField("ZipPlus4Start", validators=[DataRequired()], render_kw={"placeholder": "ZipPlus4Start"})
    ZipEnd = IntegerField("ZipPlus4End", validators=[DataRequired()], render_kw={"placeholder": "ZipPlus4End"})
    submit = SubmitField()

class UpdatePrecinctForm(FlaskForm):
    PID = IntegerField("Precinct ID", validators=[DataRequired()], render_kw={"placeholder": "PrecinctID"})
    PName = StringField("Precinct Name", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Precinct Name"})
    CandidateCount = IntegerField("Candidates Count", validators=[DataRequired()], render_kw={"placeholder": "NumofCandidates"})
    ZipCode = IntegerField("ZipCode", validators=[DataRequired()], render_kw={"placeholder": "ZipCode"})
    ZipStart = IntegerField("ZipPlus4Start", validators=[DataRequired()], render_kw={"placeholder": "ZipPlus4Start"})
    ZipEnd = IntegerField("ZipPlus4End", validators=[DataRequired()], render_kw={"placeholder": "ZipPlus4End"})
    submit = SubmitField()

class DeletePrecinctForm(FlaskForm):
    PID = IntegerField("Precinct ID", validators=[DataRequired()], render_kw={"placeholder": "PrecinctID"})
    PName = StringField("Precinct Name", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Precinct Name"})
    submit = SubmitField()

class NewRaceForm(FlaskForm):
    RaceName =StringField("Race Name", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Race Name"})
    Term = StringField("Term", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Term"})
    NumofCandidates = IntegerField("NumofCandidates", validators=[DataRequired()], render_kw={"placeholder": "NumofCandidates"})
    StartDate =DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "Start Date"})
    EndDate = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "End Date"})
    submit = SubmitField()

class UpdateRaceForm(FlaskForm):
    RaceName =StringField("Race Name", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Race Name"})
    Term = StringField("Term", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Term"})
    NumofCandidates = IntegerField("NumofCandidates", validators=[DataRequired()], render_kw={"placeholder": "NumofCandidates"})
    StartDate =DateField('Start Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "Start Date"})
    EndDate = DateField('End Date', format='%Y-%m-%d', validators=[DataRequired()], render_kw={"placeholder": "End Date"})
    submit = SubmitField()

class DeleteRaceForm(FlaskForm):
    RaceName =StringField("Race Name", validators=[DataRequired(), Length(1, 20)], render_kw={"placeholder": "Race Name"})
    submit = SubmitField()

class ElectionForm(FlaskForm):
    election_title = StringField('Election Title', validators=[DataRequired()], render_kw={'placeholder': 'Election Title'})
    geography = StringField('Geography', validators=[DataRequired()], render_kw={'placeholder': 'Geography'})
    electoral_constituency = StringField('Electoral Constituency', validators=[DataRequired()], render_kw={'placeholder': 'Electoral Constituency'})
    #public_status = IntegerField('Public Status', validators=[DataRequired(), EqualTo(0,1)])
    public_status = SelectField('Public Status', choices=[('0', 'Private'), ('1', 'Public')])
    submit = SubmitField()

class DeleteForm(FlaskForm):
    are_you_sure = BooleanField('Are you sure that you would like to delete this Election?')
    submit = SubmitField()

class DeleteDateForm(FlaskForm):
    are_you_sure = BooleanField('Are you sure that you would like to delete this Election Date?')
    submit = SubmitField()

class DeleteCandidateForm(FlaskForm):
    are_you_sure = BooleanField('Are you sure that you would like to delete this Candidate?')
    submit = SubmitField()


class ElectionDateForm(FlaskForm):
    start_date = DateField('Start Date', validators=[DataRequired()], render_kw={'placeholder': 'Start Date'})
    end_date = DateField('End Date', validators=[DataRequired()], render_kw={'placeholder': 'End Date'})
    submit = SubmitField()


class CandidateForm(FlaskForm):
    electoral_race = StringField('ElectoralRace', validators=[DataRequired()], render_kw={'placeholder': 'Electoral Race'})
    candidate_fn = StringField('Candidate First Name', validators=[DataRequired()], render_kw={'placeholder': 'Candidate First Name'})
    candidate_ln = StringField('Candidate Last Name', validators=[DataRequired()], render_kw={'placeholder': 'Candidate Last Name'})
    info = StringField('Candidate Information', validators=[DataRequired()], render_kw={'placeholder': 'Candidate Information'})
    submit = SubmitField()

class AddManager(FlaskForm):
    ManagerID = IntegerField('Manager ID', validators=[DataRequired()], render_kw={'placeholder': 'Manager ID'})
    PrecinctID = IntegerField('Precinct ID', validators=[DataRequired()], render_kw={'placeholder': 'Precinct ID'})
    PrecinctName = StringField('Precinct Name', validators=[DataRequired()], render_kw={'placeholder': 'Precinct Name'})
    submit = SubmitField()
