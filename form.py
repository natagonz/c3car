from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,TextAreaField, IntegerField, DateField, SelectField,SubmitField
from wtforms.validators import InputRequired, EqualTo, Email, Length
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf.file import FileField, FileAllowed, FileRequired

images = UploadSet("images",IMAGES)


class UserRegisterForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])


class UserLoginForm(FlaskForm):
	email = StringField("Email",validators=[InputRequired()])
	password = PasswordField("Password",validators=[InputRequired()])




class EditMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])	
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])	
	renew = DateField("Aktif Sampai",format="%m/%d/%Y")
	status = SelectField("Status",choices= [("aktif","aktif"),("pending","pending")])	  


class BookingStatusForm(FlaskForm):
	status = SelectField("",choices= [("Belum Cuci","Belum Cuci"),("Sedang Cuci","Sedang Cuci"),("Finish","Finish"),("Out","Out"),("Selesai","Selesai")])	


class InvoicePaymentForm(FlaskForm):
	payment = SelectField("",choices= [("Belum Lunas","Belum Lunas"),("Lunas","Lunas")])	


class DeleteAntreanForm(FlaskForm):
	submit = SubmitField("Hapus Antrean")	


class ForgotPasswordForm(FlaskForm):
	email = StringField("Email",validators=[InputRequired(),Length(max=100)]) 


class ResetPasswordForm(FlaskForm):
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6,max=100)])



class AddPackageForm(FlaskForm):
	name = StringField("Paket",validators=[Length(max=100),InputRequired()])
	regular = IntegerField("Regular",validators=[InputRequired()]) 	
	paket1 = IntegerField("Paket 1 ",validators=[InputRequired()]) 	
	paket2 = IntegerField("Paket 2",validators=[InputRequired()]) 	
	paket3 = IntegerField("Paket 3",validators=[InputRequired()]) 	
	
	
class AddGalleryForm(FlaskForm):
	image = FileField("Upload Photo",validators=[FileAllowed(images,"Images Only")])
	description = StringField("Deskripsi",validators=[Length(max=200)])





