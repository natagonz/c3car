from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,TextAreaField, IntegerField, DateField, SelectField,SubmitField
from wtforms.validators import InputRequired, EqualTo, Email, Length


class UserRegisterForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])


class UserLoginForm(FlaskForm):
	email = StringField("Email",validators=[InputRequired()])
	password = PasswordField("Password",validators=[InputRequired()])



class AddMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])
	date = DateField("Tanggal",format="%m/%d/%Y")	

class EditMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])	
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])
	date = DateField("Tanggal",format="%m/%d/%Y")	


class BookingForm(FlaskForm):
	name = StringField("Nama",validators=[Length(max=100)])
	email = StringField("Email",validators=[Length(max=100)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])



class BookingStatusForm(FlaskForm):
	status = SelectField("",choices= [("Belum Selesai","Belum Selesai"),("Selesai","Selesai")])	


class DeleteAntreanForm(FlaskForm):
  submit = SubmitField("Hapus Antrean")	


class ForgotPasswordForm(FlaskForm):
	email = StringField("Email",validators=[InputRequired(),Length(max=100)]) 


class ResetPasswordForm(FlaskForm):
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6,max=100)])
	
	






