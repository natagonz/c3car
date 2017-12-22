from flask import Flask, request, flash , session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager , UserMixin, login_user, login_required, logout_user, current_user
from form import UserRegisterForm,UserLoginForm,AddMemberForm,EditMemberForm,BookingStatusForm,DeleteAntreanForm,ForgotPasswordForm,ResetPasswordForm,AddPackageForm
from datetime import datetime,timedelta 
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer,SignatureExpired
from config import secret,databases
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,TextAreaField, IntegerField, DateField, SelectField,SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import InputRequired, EqualTo, Email, Length


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = databases
app.config["SECRET_KEY"] = secret
db = SQLAlchemy(app)
app.debug = True


#login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "UserLogin"


#fungsi mail
app.config.from_pyfile("config.py") 
mail = Mail(app)
s = URLSafeTimedSerializer("secret")





class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(100))
	email = db.Column(db.String(100))
	password = db.Column(db.String(300))
	role = db.Column(db.String(100))	
	phone = db.Column(db.String(200))
	mobil = db.Column(db.String(100))
	plat = db.Column(db.String(100))
	status = db.Column(db.String(100))
	date = db.Column(db.DateTime())
	renew = db.Column(db.DateTime())


	def is_active(self):
		return True

	def get_id(self):
		return self.id

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return False




class Book(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(200))
	email = db.Column(db.String(200))
	phone = db.Column(db.String(200))
	mobil = db.Column(db.String(100))
	plat = db.Column(db.String(100))
	status = db.Column(db.String(100))
	role = db.Column(db.String(100))
	paket = db.Column(db.String(200)) 
	date = db.Column(db.DateTime())


class Paket(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100))

	def __repr__(self):
		return '{}'.format(self.name)


def choice_query():
	return Paket.query.all()



############## form ################
class BookingForm(FlaskForm):
	name = StringField("Nama",validators=[Length(max=100)])
	email = StringField("Email",validators=[Length(max=100)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	paket = QuerySelectField(query_factory=choice_query)
	plat =  StringField("Plat",validators=[Length(max=100)])
	role = SelectField("Type",choices= [("umum","umum"),("vip","vip")])	

##############################################




#user loader
@login_manager.user_loader
def user_loader(user_id):
	return User.query.get(int(user_id))



@app.route("/",methods=["GET","POST"])
def Index():
	return render_template("index.html")




############################### User Route & function #################################
@app.route("/register",methods=["GET","POST"])
def UserRegister():
	form = UserRegisterForm()
	if form.validate_on_submit():
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="superuser")
		db.session.add(user)
		db.session.commit()

		flash("Pendaftran berhasil","success")
		return redirect(url_for("UserLogin"))	

	return render_template("user/register.html",form=form)	


@app.route("/login",methods=["GET","POST"])	
def UserLogin():
	form = UserLoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user :
			if check_password_hash(user.password,form.password.data):
				login_user(user)
				flash("Anda berhasil masuk","success")
				return redirect(url_for("AdminDashboard"))
		flash("Email atau Password salah","danger")
	
	return render_template("user/login.html",form=form)		




@app.route("/logout",methods=["GET","POST"])
@login_required
def Logout():
	logout_user()	
	return redirect(url_for("Index")) 	



@app.route("/forgot-password",methods=["GET","POST"])
def ForgotPassword():
	form = ForgotPasswordForm()
	if form.validate_on_submit():
		email = form.email.data
		user = User.query.filter_by(email=email).first()
		if user :
			token = s.dumps(email, salt="email-confirm")

			msg = Message("Reset Password", sender="kerjasales.com@gmail.com", recipients=[email])

			link = url_for("ResetPassword", token=token, _external=True)

			msg.body = "your link is {}".format(link)
			mail.send(msg)		
			
			return redirect(url_for("AfterForgotPassword"))
		else :
			flash("Email tidak terdaftar","danger")

	return render_template("user/forgot_password.html",form=form)


@app.route("/cek-email")
def AfterForgotPassword():
	return render_template("user/after_forgotpassword.html")




@app.route("/reset-password/<token>",methods=["GET","POST"])
def ResetPassword(token):
	form = ResetPasswordForm()
	try :
		email = s.loads(token, salt="email-confirm", max_age=3000)
		if form.validate_on_submit():
			user = User.query.filter_by(email=email).first()
			hass_pass = generate_password_hash(form.password.data,method="sha256")
			user.password = hass_pass
			db.session.commit()

			flash("Password berhasil di rubah","success")
			return redirect(url_for("UserLogin"))
	except :
		flash("Link telah expired","danger")
		return redirect(url_for("ForgotPassword"))

	return render_template("user/reset_password.html",form=form)	





@app.route("/dashboard/reset-password",methods=["GET","POST"])
@login_required
def UserResetPassword():
	user = User.query.filter_by(id=current_user.id).first()
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hass = generate_password_hash(form.password.data,method="sha256")
		user.password = hass 
		db.session.commit()
		flash("Password telah diganti","success")
	return render_template("user/user_reset_password.html",form=form)	





@app.route("/dashboard",methods=["GET","POST"])
@login_required
def AdminDashboard():
	antrean = Book.query.order_by(Book.status.desc(),Book.role.desc()).all()
	user = len(Book.query.filter_by(status="Belum Selesai").all())
	member = len(User.query.filter_by(role="member").all())	
	return render_template("user/dashboard.html",antrean=antrean,user=user,member=member)



############## admin with user function ##########
@app.route("/dashboard/user",methods=["GET","POST"])
@login_required
def AllUser():
	users = User.query.filter_by(status="user").all()
	return render_template("user/all_admin.html",users=users)	



@app.route("/dashboard/add-user",methods=["GET","POST"])
@login_required
def AdminAddUser():
	form = UserRegisterForm()
	if form.validate_on_submit():		
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="user",status="user")
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("Email telah terdaftar","danger")
		else :	
			db.session.add(user)
			db.session.commit()
			flash("User berhasil di tambah","success")
			return redirect(url_for("AllUser"))
	return render_template("user/add_user.html",form=form)



@app.route("/dashboard/delete-user/<string:id>",methods=["GET","POST"])
@login_required
def DeleteUser(id):
	user = User.query.filter_by(id=id).first()
	db.session.delete(user)
	db.session.commit()
	flash("User telah di hapus","success")	
	return redirect(url_for("AllUser"))		








############################## Member Function ###############################
@app.route("/dashboard/add-member",methods=["GET","POST"])
@login_required
def AddMember():
	form = AddMemberForm()
	if form.validate_on_submit():
		today = datetime.today()
		renew_date = today + timedelta(days=365)
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="pending",date=today,renew=renew_date)
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("email telah terdaftar","danger")
		else :			
			db.session.add(user)
			db.session.commit()
			flash("member berhasil di tambah","success")
			return redirect(url_for("AllMember"))
	return render_template("user/add_member.html",form=form)	




@app.route("/dashboard/member",methods=["GET","POST"])
@login_required
def AllMember():
	members = User.query.filter_by(role="member").all()
	return render_template("user/all_member.html",members=members)		



@app.route("/dashboard/member/<string:id>",methods=["GET","POST"])
@login_required
def MemberId(id):
	member = User.query.filter_by(id=id).first()
	if member.role == "user" or member.role == "superuser" :
		return "no access"		
	else :		
		return render_template("user/member_id.html",member=member)



@app.route("/dashboard/edit-member/<string:id>",methods=["GET","POST"])
@login_required
def EditMember(id):
	member = User.query.filter_by(id=id).first()
	
	if member.role == "superuser" or member.role == "user":
		return "no access"
	else :	
		form = EditMemberForm()
		form.username.data = member.username
		form.email.data = member.email			
		form.phone.data = member.phone			
		form.mobil.data = member.mobil
		form.plat.data = member.plat			
		form.date.data = member.date
		form.renew.data = member.renew	
		if form.validate_on_submit():
			date = datetime.strptime(request.form["date"], '%m/%d/%Y').strftime('%Y-%m-%d')	
			renew_date = datetime.strptime(request.form["renew"], '%m/%d/%Y').strftime('%Y-%m-%d')	
			member.username = request.form["username"]
			member.email = request.form["email"]			
			member.phone = request.form["phone"]			
		 	member.mobil = request.form["mobil"]
		 	member.plat	= request.form["plat"]		
			member.date	= date
			member.renew = renew_date
			db.session.commit()
			flash("Member berhasil di edit","success")
			return redirect(url_for("AllMember"))		
	return render_template("user/edit_member.html",form=form)	

@app.route("/dashboard/delete-member/<string:id>",methods=["GET","POST"])
@login_required
def DeleteMember(id):
	member = User.query.filter_by(id=id).first()
	if member.role == "superuser" or member.role == "user":
		return "no access"
	else:
		db.session.delete(member)
		db.session.commit()
		flash("Member berhasil di hapus","success")
		return redirect(url_for("AllMember"))		
			
			

###################################### Member route ############################
@app.route("/dashboard/booking",methods=["GET","POST"])
@login_required
def Booking():
	form = BookingForm()
	if form.validate_on_submit():
		if current_user.role == "user" or current_user.role  == "superuser":
			today = datetime.today()			
			book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,paket=form.paket.data,status="Belum Selesai",role=form.role.data)
			db.session.add(book)
			db.session.commit()
			flash("Booking berhasil","success")
			return redirect(url_for("Antrean"))
		else :
			today = datetime.today()			
			book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,paket=form.paket.data,status="Belum Selesai",role="vip")
			db.session.add(book)
			db.session.commit()
			flash("Booking berhasil","success")
			return redirect(url_for("Antrean"))
			
	return render_template("user/booking.html",form=form)	


@app.route("/dashboard/antrean",methods=["GET","POST"])
@login_required
def Antrean():
	antrean = Book.query.order_by(Book.status.desc(),Book.role.desc()).all()
	return render_template("user/antrean.html",antrean=antrean)



@app.route("/dashboard/edit-antrean/<string:id>",methods=["GET","POST"])
@login_required
def EditAntrean(id):
	form = BookingStatusForm()
	antre = Book.query.filter_by(id=id).first()
	form.status.data = antre.status
	if form.validate_on_submit():
		antre.status = request.form["status"]
		db.session.commit()
		flash("Status berhasil di update","success")
		return redirect(url_for("Antrean"))
	return render_template("user/edit_antrean.html",form=form)	







@app.route("/dashboard/delete-antrean",methods=["GET","POST"])
@login_required
def DeleteAllBooking():
	form = DeleteAntreanForm()
	if form.validate_on_submit():
		db.session.query(Book).delete()
		db.session.commit()
		flash("Antrean berhasil di hapus","success")
		return redirect(url_for("Antrean"))
	return render_template("user/delete_antrean.html",form=form)	





@app.route("/dashboard/add-package",methods=["GET","POST"])
@login_required
def AddPackage():
	form = AddPackageForm()
	if form.validate_on_submit():
		paket = Paket(name=form.name.data)
		db.session.add(paket)
		db.session.commit()
		flash("Paket berhasil di tambahkan","success")
		return redirect(url_for("AllPackage"))
	return render_template("user/add_package.html",form=form) 	



@app.route("/dashboard/edit-package/<string:id>",methods=["GET","POST"])
@login_required
def EditPackage(id):
	form = AddPackageForm()
	pack = Paket.query.filter_by(id=id).first()
	form.name.data = pack.name 
	if form.validate_on_submit():
		pack.name = request.form["name"]
		db.session.commit()
		flash("Paket berhasil di rubah","success")
		return redirect(url_for("AllPackage"))
	return render_template("user/edit_package.html",form=form)	




@app.route("/dashboard/delete-package/<string:id>",methods=["GET","POST"])
@login_required
def DeletePackage(id):	
	paket = Paket.query.filter_by(id=id).first()
	db.session.delete(paket)
	db.session.commit()
	flash("Paket berhasil di hapus","success")
	return redirect(url_for("AllPackage"))




@app.route("/dashboard/package",methods=["GET","POST"])
@login_required
def AllPackage():
	pakets = Paket.query.all()
	return render_template("user/package.html",pakets=pakets)











if __name__ == "__main__":
	app.run(host='0.0.0.0')
