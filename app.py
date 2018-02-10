from flask import Flask, request, flash , session, render_template, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager , UserMixin, login_user, login_required, logout_user, current_user
from form import UserRegisterForm,UserLoginForm,EditMemberForm,BookingStatusForm,DeleteAntreanForm,ForgotPasswordForm,ResetPasswordForm,AddPackageForm,AddGalleryForm,InvoicePaymentForm
from datetime import datetime,timedelta 
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer,SignatureExpired
from config import secret,databases
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,TextAreaField, IntegerField, DateField, SelectField,SubmitField,SelectMultipleField,FieldList
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import InputRequired, EqualTo, Email, Length
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf.file import FileField, FileAllowed, FileRequired
import pdfkit


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

#fungsi Upload
#mengatur image
images = UploadSet("images",IMAGES)
app.config["UPLOADED_IMAGES_DEST"] = "static/img/profile/"
app.config["UPLOADED_IMAGES_URL"] = "http://127.0.0.1:5000/static/img/profile/"
configure_uploads(app,images)



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
	location = db.Column(db.String(200))
	member = db.Column(db.String(200))
	paket = db.Column(db.String(200))		


	def is_active(self):
		return True

	def get_id(self):
		return self.id

	def is_authenticated(self):
		return self.authenticated

	def is_anonymous(self):
		return False

	def __repr__(self):
		return '{}'.format(self.username)	




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
	price = db.Column(db.Integer())
	owner = db.Column(db.Integer())
	location = db.Column(db.String(200))
	payment = db.Column(db.String(200))


class Paket(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100))
	regular = db.Column(db.Integer())
	paket1 = db.Column(db.Integer())
	paket2 = db.Column(db.Integer())
	paket3 = db.Column(db.Integer())

	def __repr__(self):
		return '{}'.format(self.name)


def choice_query():
	return Paket.query.all()




class Location(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	location = db.Column(db.String(200))
	total = db.Column(db.Integer())

	def __repr__(self):
		return '{}'.format(self.location)


def location_query():
	return Location.query.all()			


def cashier_query():	
	return User.query.filter_by(role="cashier").all()



class Gallery(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	image_name = db.Column(db.String(200))
	description = db.Column(db.String(200)) 



class Accounting(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	description = db.Column(db.String(300))
	location = db.Column(db.String(300))
	amount = db.Column(db.Integer())
	status = db.Column(db.String(200))
	date = db.Column(db.DateTime())
	cashier = db.Column(db.String(200))





############## form ################
class BookingForm(FlaskForm):
	name = StringField("Nama",validators=[Length(max=100)])
	email = StringField("Email",validators=[Length(max=100)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	paket = QuerySelectField(query_factory=choice_query)		
	plat =  StringField("Plat",validators=[Length(max=100)])	
	location = QuerySelectField(query_factory=location_query)



class UserBookingForm(FlaskForm):
	name = StringField("Nama",validators=[Length(max=100)])
	email = StringField("Email",validators=[Length(max=100)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	paket = QuerySelectField(query_factory=choice_query)
	plat =  StringField("Plat",validators=[Length(max=100)])
	role = StringField("Type",validators=[Length(max=100)])	
	location = QuerySelectField(query_factory=location_query)


class AddMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])
	location = QuerySelectField(query_factory=location_query)
	paket = SelectField("Paket",choices= [("paket1","paket1"),("paket2","paket2"),("paket3","paket3")])




class AddAdminForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])
	location = QuerySelectField(query_factory=location_query)

class AddLocationForm(FlaskForm):
	location = StringField("Location",validators=[Length(max=200),InputRequired()])



class AddAccountingForm(FlaskForm):
	description = StringField("Description",validators=[InputRequired(),Length(max=300)])
	amount = IntegerField("Jumlah",validators=[InputRequired()])
	

class SuperUserAddAccountingForm(FlaskForm):
	description = StringField("Description",validators=[InputRequired(),Length(max=300)])
	amount = IntegerField("Jumlah",validators=[InputRequired()])
	location = QuerySelectField(query_factory=location_query)



class AccountingSearchForm(FlaskForm):
	start = DateField("Dari",format="%m/%d/%Y")
	end = DateField("Sampai",format="%m/%d/%Y")	


class TopUpForm(FlaskForm):
	paket = SelectField("Paket",choices= [("paket1","paket1"),("paket2","paket2")])




##############################################




#user loader
@login_manager.user_loader
def user_loader(user_id):
	return User.query.get(int(user_id))



@app.route("/",methods=["GET","POST"])
def Index():
	return render_template("index.html")


@app.route("/gallery",methods=["GET","POST"])
def FrontGallery():
	gallerys = Gallery.query.all()
	return render_template("gallery.html",gallerys=gallerys)




####################### Accounting ###########################

@app.route("/dashboard/add-income",methods=["GET","POST"])
@login_required
def AddIncome():
	if current_user.role == "superuser" or current_user.role == "accountant" :
		form = SuperUserAddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			income = Accounting(description=form.description.data,location=form.location.data,amount=form.amount.data,date=today,status="Income")
			db.session.add(income)
			db.session.commit()
			flash("Pendapatan berhasil di input","success")
			return redirect(url_for("AdminDashboard"))
	else :
		form = AddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			income = Accounting(description=form.description.data,location=current_user.location,amount=form.amount.data,date=today,status="Income")
			db.session.add(income)
			db.session.commit()
			flash("Pendapatan berhasil di input","success")
			return redirect(url_for("AdminDashboard"))			
	return render_template("user/add_income.html",form=form)	



@app.route("/dashboard/add-expense",methods=["GET","POST"])
@login_required
def AddExpense():
	if current_user.role == "superuser" or current_user.role == "accountant":
		form = SuperUserAddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			expense = Accounting(description=form.description.data,location=form.location.data,amount=form.amount.data,date=today,status="Expense")
			db.session.add(expense)
			db.session.commit()
			flash("Pengeluaran berhasil di input","success")
			return redirect(url_for("AdminDashboard"))
	else :	
		form = AddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			expense = Accounting(description=form.description.data,location=current_user.location,amount=form.amount.data,date=today,status="Expense")
			db.session.add(expense)
			db.session.commit()
			flash("Pengeluaran berhasil di input","success")
			return redirect(url_for("AdminDashboard"))
	return render_template("user/add_expense.html",form=form)	



@app.route("/dashboard/location/transaction",methods=["GET","POST"])
@login_required
def AllLocationTransaction():
	locations = Location.query.all()		
	return render_template("user/all_location_transaction.html",locations=locations) 


@app.route("/dashboard/location/transaction/<string:id>",methods=["GET","POST"])
@login_required
def Transaction(id):
	location = Location.query.filter_by(id=id).first()
	name = location.location
	transactions = Accounting.query.filter_by(location=name).all()	
	form = AccountingSearchForm()
	if form.validate_on_submit():
		start = form.start.data
		end = form.end.data
		transactions = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name).all()
		return render_template("user/all_transaction.html",transactions=transactions,form=form,name=name)
	return render_template("user/all_transaction.html",transactions=transactions,form=form,name=name)



############ Transaksi per kasir ########################
@app.route("/dashboard/cashier/transaction/<string:id>",methods=["GET","POST"])
@login_required
def CashierTransaction(id):
	cashier = User.query.filter_by(id=id).first()
	name = cashier.username
	transactions = Accounting.query.filter_by(cashier=name).all()
	income = Accounting.query.filter_by(cashier=name,status="Income").all()
	form = AccountingSearchForm()
	if form.validate_on_submit():
		start = form.start.data
		end = form.end.data
		transactions = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.cashier == name).all()
		income = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.cashier == name,Accounting.status == "Income").all()
		return render_template("user/cashier_transaction.html",transactions=transactions,form=form,name=name,income=income)
	return render_template("user/cashier_transaction.html",transactions=transactions,form=form,name=name,income=income)	



@app.route("/dashboard/delete-transaction/<string:id>",methods=["GET","POST"])
@login_required
def DeleteTransaction(id):
	trans = Accounting.query.filter_by(id=id).first()
	db.session.delete(trans)
	db.session.commit()
	flash("Transaksi berhasil di hapus","success")
	return redirect(url_for("AllLocationTransaction"))




@app.route("/dashboard/edit-transaction/<string:id>",methods=["GET","POST"])
@login_required
def EditTransaction(id):
	form = AddAccountingForm()
	trans = Accounting.query.filter_by(id=id).first()
	form.description.data = trans.description
	form.amount.data = trans.amount	
	stats = trans.status	
	if form.validate_on_submit():		
		trans.description = request.form["description"]
		trans.amount = request.form["amount"]		
		db.session.commit()
		flash("Data berhasil di edit","success")
		return redirect(url_for("AllLocationTransaction"))
	return render_template("user/edit_transaction.html",form=form,stats=stats)	






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
	antreanx = Book.query.order_by(Book.status.desc(),Book.role.desc()).all()
	user = len(Book.query.filter_by(status="Belum Selesai").all())
	member = len(User.query.filter_by(role="member").all())
	locations = Location.query.all()  	
	return render_template("user/dashboard.html",antreanx=antreanx,user=user,member=member,locations=locations)



############## admin with user function ##########
@app.route("/dashboard/user",methods=["GET","POST"])
@login_required
def AllUser():
	users = User.query.filter_by(role="user").all()
	return render_template("user/all_admin.html",users=users)	



@app.route("/dashboard/add-user",methods=["GET","POST"])
@login_required
def AdminAddUser():
	form = AddAdminForm()
	if form.validate_on_submit():		
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="user",status="user",location=form.location.data)
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

############################## kasir ######################################

@app.route("/dashboard/cashier",methods=["GET","POST"])
@login_required
def AllCashier():
	cashiers = User.query.filter_by(role="cashier").all()
	return render_template("user/all_cashier.html",cashiers=cashiers)


@app.route("/dashboard/add-cashier",methods=["GET","POST"])
@login_required
def AddCashier():
	form = AddAdminForm()
	if form.validate_on_submit():
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="cashier",status="user",location=form.location.data)
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("Email telah terdaftar","danger")
		else :
			db.session.add(user)
			db.session.commit()
			flash("Kasir berhasil di tambahkan","success")
			return redirect(url_for("AllCashier"))
	return render_template("user/add_user.html",form=form)		
		

#################### akuntan #############
@app.route("/dashboard/add-accountant",methods=["GET","POST"])
@login_required
def AddAccountant():
	form = AddAdminForm()
	if form.validate_on_submit():
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="accountant",status="user",location=form.location.data)
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("Email telah terdaftar","danger")	
		else :
			db.session.add(user)
			db.session.commit()
			flash("Akuntan berhasil di tambah","success")
			return redirect(url_for("AllAccountant"))
	return render_template("user/add_user.html",form=form)			

@app.route("/dashboard/accountant",methods=["GET","POST"])
@login_required
def AllAccountant():
	akuntans = User.query.filter_by(role="accountant").all()
	return render_template("user/all_accountant.html",akuntans=akuntans)




############################## Member Function ###############################
@app.route("/dashboard/add-member",methods=["GET","POST"])
@login_required
def AddMember():
	form = AddMemberForm()
	if form.validate_on_submit():
		today = datetime.today()
		select = form.paket.data
		hass = generate_password_hash(form.password.data,method="sha256")		
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("email telah terdaftar","danger")
		else :	
			if select == "paket1":
				renew = today + timedelta(days=180) 
				user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="aktif",date=today,renew=renew,location=form.location.data,member="nonregular",paket="paket1")
				db.session.add(user)
				db.session.commit()
				flash("member berhasil di tambah","success")
				return redirect(url_for("AllMember"))
			elif select == "paket2":
				renew = today + timedelta(days=90) 
				user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="aktif",date=today,renew=renew,location=form.location.data,member="regular",paket="paket2")
				db.session.add(user)
				db.session.commit()
				flash("member berhasil di tambah","success")
				return redirect(url_for("AllMember"))					
			else :
				renew = today + timedelta(days=300) 
				user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="aktif",date=today,renew=renew,location=form.location.data,member="vip",paket="paket3")
				db.session.add(user)
				db.session.commit()
				flash("member berhasil di tambah","success")
				return redirect(url_for("AllMember"))				
				
	return render_template("user/add_member.html",form=form)	



@app.route("/dashboard/member",methods=["GET","POST"])
@login_required
def AllMember():
	locations = Location.query.all()
	members = User.query.filter_by(role="member").all()
	return render_template("user/all_member.html",members=members,locations=locations)	


### member berdasarkan lokasi
@app.route("/dashboard/member/location/<string:id>",methods=["GET","POST"])
@login_required
def MemberBasedLocation(id):
	location = Location.query.filter_by(id=id).first()
	members = User.query.filter_by(location=location.location,role="member").all()
	total = len(members)
	return render_template("user/member_based_location.html",members=members,total=total)


@app.route("/dashboard/member/top-up/<string:id>",methods=["GET","POST"])
@login_required
def TopUpMember(id):
	form = TopUpForm()
	member = User.query.filter_by(id=id).first()
	if form.validate_on_submit():
		select = form.paket.data 
		if select == "paket1":
			member.renew = member.renew + timedelta(days=90)
			member.status = "aktif"
			db.session.commit()
			flash("Top Up Berhasil","success")
			return redirect(url_for("AllMember"))
		else :
			member.renew = member.renew + timedelta(days=300)
			member.status = "aktif"
			db.session.commit()
			flash("Top Up Berhasil","success")
			return redirect(url_for("AllMember"))
	return render_template("user/topup_member.html",form=form)		
			






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
		form.renew.data = member.renew	
		form.status.data = member.status
		if form.validate_on_submit():			
			renew_date = datetime.strptime(request.form["renew"], '%m/%d/%Y').strftime('%Y-%m-%d')	
			member.username = request.form["username"]
			member.email = request.form["email"]			
			member.phone = request.form["phone"]			
		 	member.mobil = request.form["mobil"]
		 	member.plat	= request.form["plat"]				
			member.renew = renew_date
			member.status = request.form["status"]
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

############################# Booking Dari Admin ########################
@app.route("/dashboard/admin-booking",methods=["GET","POST"])
@login_required
def AdminBooking():
	return render_template("user/admin_booking.html")



@app.route("/dashboard/admin-booking/regular",methods=["GET","POST"])
@login_required
def AdminBookingRegular():
	form = BookingForm()
	if form.validate_on_submit():			
		today = datetime.today()					
		book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,paket=form.paket.data,status="Belum Selesai",role="regular",owner=current_user.id,location=form.location.data,payment="Belum Lunas")
		db.session.add(book)
		db.session.commit()
		flash("Booking berhasil","success")
		return redirect(url_for("AntreanLocation"))
	return render_template("user/booking.html",form=form)	


@app.route("/dashboard/admin-booking/member",methods=["GET","POST"])
@login_required
def AdminBookingMember():
	form = BookingForm()
	if form.validate_on_submit():
		member = User.query.filter_by(email=form.email.data).first()
		members = User.query.filter_by(email=form.email.data).all()
		today = datetime.today()
		check_user = len(members)	

		if check_user == 0 :
			flash("Tidak ada member yang terdaftar atas email tersebut","danger")	
		elif member.renew == today or today > member.renew :
			flash("Masa berlaku membership telah habis,silakan di perpanjang","danger")	
		else :									
			book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,paket=form.paket.data,status="Belum Selesai",role=member.member,owner=member.id,location=form.location.data,payment="Belum Lunas")
			db.session.add(book)
			db.session.commit()
			flash("Booking berhasil","success")
			return redirect(url_for("AntreanLocation"))
	return render_template("user/booking.html",form=form)	



			
			

###################################### Member route ############################
@app.route("/dashboard/booking",methods=["GET","POST"])
@login_required
def Booking():	
	today = datetime.today()
	if today > current_user.renew and current_user.status == "pending":
		return redirect(url_for("PaymentInfo"))		
	else :
		form = UserBookingForm()
		if form.validate_on_submit():
			today = datetime.today()		 				
			book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,paket=form.paket.data,status="Belum Selesai",role=current_user.member,owner=current_user.id,location=form.location.data,payment="Belum Lunas")
			db.session.add(book)
			db.session.commit()		
			flash("Booking berhasil","success")
			return redirect(url_for("AntreanLocation"))		
					
	return render_template("user/booking.html",form=form)	



###############################################################
@app.route("/dashboard/location/antrean",methods=["GET","POST"])
@login_required
def AntreanLocation():
	locations = Location.query.all()
	userlocations = Location.query.filter_by(location=current_user.location).all() 
	return render_template("user/antrean_location.html",locations=locations,userlocations=userlocations)




###############################################################

@app.route("/dashboard/antrean/<string:id>",methods=["GET","POST"])
@login_required
def Antrean(id):
	location = Location.query.filter_by(id=id).first()
	nama = location.location	
	antrean = Book.query.filter(Book.location == nama,Book.status =="Belum Selesai",Book.role != "nonregular").order_by(Book.status.desc(),Book.role.desc()).all()
	nonregulars = Book.query.filter(Book.location == nama, Book.status == "Belum Selesai", Book.role == "nonregular").all()
	total = len(antrean)
	jumlah = len(nonregulars)
	return render_template("user/antrean.html",antrean=antrean,total=total,nonregulars=nonregulars,jumlah=jumlah)




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
		return redirect(url_for("AntreanLocation"))
	return render_template("user/edit_antrean.html",form=form)	







@app.route("/dashboard/delete-antrean",methods=["GET","POST"])
@login_required
def DeleteAllBooking():
	form = DeleteAntreanForm()
	if form.validate_on_submit():
		db.session.query(Book).delete()
		db.session.commit()
		flash("Antrean berhasil di hapus","success")
		return redirect(url_for("AntreanLocation"))
	return render_template("user/delete_antrean.html",form=form)	





@app.route("/dashboard/add-package",methods=["GET","POST"])
@login_required
def AddPackage():
	form = AddPackageForm()
	if form.validate_on_submit():
		paket = Paket(name=form.name.data,regular=form.regular.data,paket1=form.paket1.data,paket2=form.paket2.data,paket3=form.paket3.data)
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
	form.price.data = pack.price
	if form.validate_on_submit():
		pack.name = request.form["name"]
		pack.price = request.form["price"]
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




############################### Gallery ##########################

@app.route("/dashboard/add-gallery",methods=["GET","POST"])
@login_required
def AddGallery():
	form = AddGalleryForm()
	if form.validate_on_submit():
		filename = images.save(form.image.data)
		gallery = Gallery(image_name=filename,description=form.description.data)
		db.session.add(gallery)
		db.session.commit()
		flash("Gambar berhasil di tambah","success")
		return redirect(url_for("AllGallery"))
	return render_template("user/add_gallery.html",form=form)	


@app.route("/dashboard/gallery",methods=["GET","POST"])
@login_required
def AllGallery():
	gallerys = Gallery.query.all()
	return render_template("user/gallery.html",gallerys=gallerys)



@app.route("/dashboard/delete-gallery/<string:id>",methods=["GET","POST"])
@login_required
def DeleteGallery(id):
	gall = Gallery.query.filter_by(id=id).first()
	db.session.delete(gall)
	db.session.commit()
	flash("gambar berhasil di hapus","success")
	return redirect(url_for("AllGallery"))	



################################## Invoice #######
### Semua Lokasi invoice
@app.route("/dashboard/location/invoice",methods=["GET","POST"])	
@login_required
def InvoiceLocation():
	locations = Location.query.all()
	userlocations = Location.query.filter_by(location=current_user.location).all()
	return render_template("user/all_invoice_location.html",locations=locations,userlocations=userlocations) 


##### invoice berdasakan lokasi
@app.route("/dashboard/location/invoice/<string:id>",methods=["GET","POST"])
@login_required
def AllInvoice(id):
	locations = Location.query.filter_by(id=id).first()
	locname = locations.location
	invoices = Book.query.filter_by(location=locname).all()
	userinvoice = Book.query.filter_by(owner=current_user.id).all()
	return render_template("user/all_invoice.html",invoices=invoices,userinvoice=userinvoice)	



#Tiap buah invoice untuk admin dan member
'''@app.route("/dashboard/invoice/<string:id>",methods=["GET","POST"])
@login_required
def UserInvoice(id): 	
	invoice = Book.query.filter_by(id=id).first()
	user = User.query.filter_by(id=invoice.owner).first()
	paket = Paket.query.filter_by(name=invoice.paket).first()	
	if user.paket == "paket1":
		total = paket.paket1
		harga = "{:,}".format(total).replace(",",".")
		return render_template("user/invoice.html",invoice=invoice,paket=paket,harga=harga)
	elif user.paket == "paket2":
		total = paket.paket2
		harga = "{:,}".format(total).replace(",",".")
		return render_template("user/invoice.html",invoice=invoice,paket=paket,harga=harga)
	elif user.paket == "paket3":
		total = paket.paket3
		harga = "{:,}".format(total).replace(",",".")
		return render_template("user/invoice.html",invoice=invoice,paket=paket,harga=harga)
	else :		
		total = paket.regular
		harga = "{:,}".format(total).replace(",",".")
		return render_template("user/invoice.html",invoice=invoice,paket=paket,harga=harga)'''


@app.route("/dashboard/invoice/<string:id>",methods=["GET","POST"])
@login_required
def UserInvoice(id):
	invoice = Book.query.filter_by(id=id).first()
	user = User.query.filter_by(id=invoice.owner).first()
	paket = Paket.query.filter_by(name=invoice.paket).first()
	css = "invoice.css"	
	if invoice.payment == "Belum Lunas":
		paket = Paket.query.filter_by(name=invoice.paket).first()			
		loc = invoice.location		
		today = datetime.today()
		invoice.payment = "Lunas"
		if user.paket == "paket1":
			total = paket.paket1
			harga = "{:,}".format(total).replace(",",".")	
			membership = user.renew
			amount = paket.paket1
			trans = Accounting(description="Pembayaran dari customer",amount=amount,date=today,location=loc,status="Income",cashier=current_user.username)
			db.session.add(trans)
			db.session.commit()
			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False, css=css)		
			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
		elif user.paket == "paket2":
			total = paket.paket2
			harga = "{:,}".format(total).replace(",",".")		
			membership = user.renew
			amount = paket.paket2
			trans = Accounting(description="Pembayaran dari customer",amount=amount,date=today,location=loc,status="Income",cashier=current_user.username)
			db.session.add(trans)
			db.session.commit()

			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False,css=css)

			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
		elif user.paket == "paket3":
			total = paket.paket3
			harga = "{:,}".format(total).replace(",",".")		
			membership = user.renew
			amount = paket.paket3
			trans = Accounting(description="Pembayaran dari customer",amount=amount,date=today,location=loc,status="Income",cashier=current_user.username)
			db.session.add(trans)
			db.session.commit()

			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False ,css=css)

			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
		else :		
			total = paket.regular
			harga = "{:,}".format(total).replace(",",".")
			membership = user.renew
			amount = paket.regular
			trans = Accounting(description="Pembayaran dari customer",amount=amount,date=today,location=loc,status="Income",cashier=current_user.username)
			db.session.add(trans)
			db.session.commit()


			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False,css=css)


			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
	else:	
		if user.paket == "paket1":
			total = paket.paket1
			harga = "{:,}".format(total).replace(",",".")	
			membership = user.renew

			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False, css=css)		
			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
		elif user.paket == "paket2":
			total = paket.paket2
			harga = "{:,}".format(total).replace(",",".")		
			membership = user.renew
			
			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False,css=css)

			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
		elif user.paket == "paket3":
			total = paket.paket3
			harga = "{:,}".format(total).replace(",",".")		
			membership = user.renew
			
			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False ,css=css)

			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response
		else :		
			total = paket.regular
			harga = "{:,}".format(total).replace(",",".")
			membership = user.renew
			
			rendered = render_template("user/invois.html",invoice=invoice,paket=paket,harga=harga,user=user,membership=membership)
			pdf = pdfkit.from_string(rendered, False,css=css)


			response = make_response(pdf)
			response.headers['Content-Type'] = 'application/pdf'
			response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
			return response	



#### invoice member ####
@app.route("/dashboard/invoice",methods=["GET","POST"])
@login_required
def AllMemberInvoice():
	invoices = Book.query.filter_by(owner=current_user.id).all()
	return render_template("user/member_invoice.html",invoices=invoices)




####### edit invoice payment ###########
'''@app.route("/dashboard/edit-invoice/<string:id>",methods=["GET","POST"])
@login_required
def EditInvoicePayment(id):
	form = InvoicePaymentForm()
	invoice = Book.query.filter_by(id=id).first()
	user = User.query.filter_by(id=invoice.owner).first()
	form.payment.data = invoice.payment
	if invoice.payment == "Belum Lunas":
		if form.validate_on_submit():
			pay = request.form["payment"]
			paket = Paket.query.filter_by(name=invoice.paket).first()			
			loc = invoice.location		
			today = datetime.today()
			invoice.payment = pay
			if pay == "Lunas":
				if user.paket == "paket1":
					harga = paket.paket1
					trans = Accounting(description="Pembayaran dari customer",amount=harga,date=today,location=loc,status="Income",cashier=current_user.username)
					db.session.add(trans)
					db.session.commit()
					flash("Status pembayaran berhasil di rubah","success")
					return redirect(url_for("InvoiceLocation"))	
				elif user.paket == "paket2":
					harga = paket.paket2
					trans = Accounting(description="Pembayaran dari customer",amount=harga,date=today,location=loc,status="Income",cashier=current_user.username)
					db.session.add(trans)
					db.session.commit()
					flash("Status pembayaran berhasil di rubah","success")
					return redirect(url_for("InvoiceLocation"))
				elif user.paket == "paket3":
					harga = paket.paket3
					trans = Accounting(description="Pembayaran dari customer",amount=harga,date=today,location=loc,status="Income",cashier=current_user.username)
					db.session.add(trans)
					db.session.commit()
					flash("Status pembayaran berhasil di rubah","success")
					return redirect(url_for("InvoiceLocation"))	
				else:
					harga = paket.regular
					trans = Accounting(description="Pembayaran dari customer",amount=harga,date=today,location=loc,status="Income",cashier=current_user.username)
					db.session.add(trans)
					db.session.commit()
					flash("Status pembayaran berhasil di rubah","success")
					return redirect(url_for("InvoiceLocation"))								
	else :
		if form.validate_on_submit():			
			flash("Status pembayaran tidak bisa di rubah karena sudah lunas","danger")		
				
	return render_template("user/edit_invoice_payment.html",form=form)		
'''



########################### Location ##########################

@app.route("/dashboard/add-location",methods=["GET","POST"])
@login_required
def AddLocation():
	form = AddLocationForm()
	if form.validate_on_submit():
		loc = Location(location=form.location.data,total=0)
		db.session.add(loc)
		db.session.commit()
		flash("Lokasi berhasil di tambah","success")
		return redirect(url_for("AdminDashboard"))
	return render_template("user/add_location.html",form=form)	

@app.route("/dashboard/all-location",methods=["GET","POST"])
@login_required
def AllLocation():
	locations = Location.query.all()
	return render_template("user/all_location.html",locations=locations)


@app.route("/dashboard/edit-location/<string:id>",methods=["GET","POST"])
@login_required
def EditLocation(id):
	form = AddLocationForm()
	location = Location.query.filter_by(id=id).first()
	form.location.data = location.location
	if form.validate_on_submit():
		location.location = request.form["location"]
		db.session.commit()
		flash("Lokasi berhasil di rubah","success")
		return redirect(url_for("AllLocation"))
	return render_template("user/edit_location.html",form=form)	



@app.route("/dashboard/delete-location/<string:id>",methods=["GET","POST"])
@login_required
def DeleteLocation(id):
	loc = Location.query.filter_by(id=id).first()
	db.session.delete(loc)
	db.session.commit()
	flash("Lokasi berhasil di hapus","success")
	return redirect(url_for("AllLocation"))	



############################### Payment info ######################
@app.route("/dashboard/info-payment")
def PaymentInfo():
	return render_template("user/payment_info.html")










if __name__ == "__main__":
	app.run(host='0.0.0.0')
