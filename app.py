from flask import Flask, request, flash , session, render_template, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager , UserMixin, login_user, login_required, logout_user, current_user
from form import UserRegisterForm,UserLoginForm,EditMemberForm,BookingStatusForm,DeleteAntreanForm,ForgotPasswordForm,ResetPasswordForm,AddPackageForm,AddGalleryForm,InvoicePaymentForm,SubmitForm
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
app.config["DEBUG"] = True
db = SQLAlchemy(app)



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
	marketing = db.Column(db.String(200))	
	treatment = db.Column(db.String(200))
	birth = db.Column(db.DateTime())


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
	tambahan = db.Column(db.String(200))	
	date = db.Column(db.DateTime())
	price = db.Column(db.Integer())
	owner = db.Column(db.Integer())
	location = db.Column(db.String(200))
	payment = db.Column(db.String(200))
	treatment = db.Column(db.String(200))
	


class Paket(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100))
	price = db.Column(db.Integer())
	status = db.Column(db.String(200))	

	def __repr__(self):
		return '{}'.format(self.name)


class BookingPaket(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	book_id = db.Column(db.Integer())	
	paket_id = db.Column(db.Integer())
	paket_name = db.Column(db.String(200))
	paket_price = db.Column(db.Integer())


class Location(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	location = db.Column(db.String(200))
	total = db.Column(db.Integer())

	def __repr__(self):
		return '{}'.format(self.location)


def location_query():
	return Location.query.all()	

def umum_query():
	return Paket.query.filter_by(status="umum").all()			


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
	pakets = db.Column(db.PickleType())
	customer = db.Column(db.String(200))
	member = db.Column(db.String(200))


class MemberPayment(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	amount = db.Column(db.Integer())
	owner = db.Column(db.String(200))
	date = db.Column(db.DateTime())




############## form ################
class BookingMemberForm(FlaskForm):
	plat = StringField("Plat",validators=[Length(max=100)])
	


class BookingForm(FlaskForm):
	name = StringField("Nama",validators=[Length(max=100)])
	email = StringField("Email",validators=[Length(max=100)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])	
	plat =  StringField("Plat",validators=[Length(max=100)])	

class YudiBookingRegularForm(FlaskForm):
	name = StringField("Nama",validators=[Length(max=100)])
	email = StringField("Email",validators=[Length(max=100)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])	
	plat =  StringField("Plat",validators=[Length(max=100)])
	location = QuerySelectField("Lokasi",query_factory=location_query)

class YudiBookingMemberForm(FlaskForm):
	plat = StringField("Plat",validators=[Length(max=100)])	
	location = QuerySelectField("Lokasi",query_factory=location_query)					



class UserBookingForm(FlaskForm):		
	location = QuerySelectField(query_factory=location_query)


class AddMemberForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])
	phone = StringField("Telepon",validators=[Length(max=100)])
	mobil = StringField("Mobil",validators=[Length(max=100)])
	plat =  StringField("Plat",validators=[Length(max=100)])
	birth = DateField("Tanggal Lahir",format="%m/%d/%Y")
	paket = SelectField("Paket",choices= [("paket1","paket1"),("paket2","paket2"),("paket3","paket3")])




class AddAdminForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])
	location = QuerySelectField(query_factory=location_query)


class AddMarketingForm(FlaskForm):
	username = StringField("Username",validators=[InputRequired(),Length(max=100)])
	email = StringField("Email",validators=[InputRequired(),Length(max=100)])
	password = PasswordField("Password",validators=[InputRequired(),Length(min=6)])


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

class DateFilter(FlaskForm):
	date = DateField("Dari",format="%m/%d/%Y") 

class EditMarketingStatusForm(FlaskForm):
	status = SelectField("Status",choices= [("aktif","aktif"),("pending","pending")]) 	


class LocationSearchForm(FlaskForm):
	search = StringField("Nama Lokasi",validators=[InputRequired(),Length(max=200)])	


class BookingStatusFormSa(FlaskForm):
	status = SelectField("",choices= [("Dalam Perjalanan","Dalam Perjalanan"),("Belum Cuci","Belum Cuci")])	





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





############ Transaksi per kasir ########################
@app.route("/dashboard/cashier/transaction/<string:id>",methods=["GET","POST"])
@login_required
def CashierTransaction(id):
	cashier = User.query.filter_by(id=id).first()
	name = cashier.username
	transactions = Accounting.query.filter_by(cashier=name).all()
	income = Accounting.query.filter_by(cashier=name,status="Income").all()
	expense = Accounting.query.filter_by(cashier=name,status="Expense").all()
	form = AccountingSearchForm()
	if form.validate_on_submit():
		start = form.start.data
		end = form.end.data
		transactions = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.cashier == name).all()
		income = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.cashier == name,Accounting.status == "Income").all()
		expense = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.cashier == name,Accounting.status == "Expense").all()
		return render_template("user/cashier_transaction.html",transactions=transactions,form=form,name=name,income=income,expense=expense)
	return render_template("user/cashier_transaction.html",transactions=transactions,form=form,name=name,income=income,expense=expense)	



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
			if user.status == "pending":
				flash("Akun anda telah pending","danger")
			else :	
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
	form = LocationSearchForm()
	if form.validate_on_submit():
		loc = form.search.data
		locations = Location.query.filter_by(location=loc).all()
		return render_template("user/dashboard.html",antreanx=antreanx,user=user,member=member,locations=locations,form=form)
	return render_template("user/dashboard.html",antreanx=antreanx,user=user,member=member,locations=locations,form=form)



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


######################### SA #########################
@app.route("/dashboard/add-sa",methods=["GET","POST"])
@login_required
def AddSa():
	form = AddAdminForm()
	if form.validate_on_submit():
		hass = generate_password_hash(form.password.data,method="sha256")
		user = User(username=form.username.data,email=form.email.data,password=hass,role="sa",status="user",location=form.location.data)
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("Email telah terdaftar","danger")
		else :
			db.session.add(user)
			db.session.commit()
			flash("SA berhasil ditambahkan","success")
			return redirect(url_for("AllSa"))
	return render_template("user/add_user.html",form=form)

@app.route("/dashboard/sa",methods=["GET","POST"])
@login_required
def AllSa():
	users = User.query.filter_by(role="sa").all()
	return render_template("user/all_sa.html",users=users)

@app.route("/dashboard/delete-sa/<string:id>",methods=["GET","POST"])
@login_required
def DeleteSa(id):
	user = User.query.filter_by(id=id).first()
	db.session.delete(user)
	db.session.commit()
	flash("User telah di hapus","success")	
	return redirect(url_for("AllSa"))			



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
		user = User(username=form.username.data,email=form.email.data,password=hass,role="cashier",status="aktif",location=form.location.data)
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


################################# Marketing #####################
@app.route("/dashboard/add-marketing",methods=["GET","POST"])
@login_required
def AddMarketing():
	form = AddMarketingForm()
	if form.validate_on_submit():
		hass = generate_password_hash(form.password.data,method="sha256")
		marketing = User(username=form.username.data,email=form.email.data,password=hass,role="marketing",status="aktif") 
		check_user = User.query.filter_by(email=form.email.data).all()
		if len(check_user) > 0 :
			flash("Email telah terdaftar","danger")
		else :
			db.session.add(marketing)
			db.session.commit()
			flash("Marketing berhasil di tambahkan","success")
			return redirect(url_for("AllMarketing"))
	return render_template("user/add_marketing.html",form=form)			


@app.route("/dashboard/marketing",methods=["GET","POST"])
@login_required
def AllMarketing():
	marketings = User.query.all()
	return render_template("user/all_marketing.html",marketings=marketings)



@app.route("/dashboard/edit-marketing/<string:id>",methods=["GET","POST"])
@login_required
def EditMarketingStatus(id):
	marketing = User.query.filter_by(id=id).first()
	form = EditMarketingStatusForm()
	form.status.data = marketing.status
	if form.validate_on_submit():
		marketing.status = request.form["status"]
		db.session.commit()
		flash("Status Berhasil di perbaharui","success")
		return redirect(url_for("AllMarketing"))
	return render_template("user/edit_marketing_status.html",form=form)	




@app.route("/dashboard/marketing/member/<string:id>",methods=["GET","POST"])
@login_required
def MarketingMember(id):
	if current_user.role == "marketing": 		
		members = User.query.filter_by(marketing=current_user.username).order_by(User.date.desc()).all()	
		total = len(members)	
		return render_template("user/marketing_members.html",members=members,total=total)
	else :
		marketing = User.query.filter_by(id=id).first()
		name = marketing.username
		members = User.query.filter_by(marketing=marketing.username).order_by(User.date.desc()).all()
		total = len(members)
		form = AccountingSearchForm()
		if form.validate_on_submit():
			start = form.start.data
			end = form.end.data 
			members = User.query.filter(User.date.between(start,end)).filter(User.marketing == name).order_by(User.date.desc()).all()
			total = len(members)
			return render_template("user/marketing_members.html",members=members,form=form,name=name,total=total)
		return render_template("user/marketing_members.html",members=members,form=form,name=name,total=total)



#history bookingan dari member
@app.route("/dashboard/marketing/member/history/<string:id>",methods=["GET","POST"])
@login_required
def BookingHistory(id):
	user = User.query.filter_by(id=id).first()
	books = Book.query.filter_by(owner=id).all() 
	return render_template("member/history.html",books=books,user=user)



@app.route("/dashboard/marketing/member/history/detail/<string:id>",methods=["GET","POST"])
@login_required
def BookingHistoryDetail(id):
	book = Book.query.filter_by(id=id).first()
	pakets = BookingPaket.query.filter_by(book_id=book.id).all()
	return render_template("member/detail.html",pakets=pakets,book=book)




@app.route("/dashboard/marketing/stats/<string:id>",methods=["GET","POST"])
@login_required
def MarketingStats(id):
	user = User.query.filter_by(id=id).first()
	name =  user.username
	transaction = MemberPayment.query.filter_by(owner=name).order_by(MemberPayment.date.desc()).all()	
	form = AccountingSearchForm()
	if form.validate_on_submit():
		start = form.start.data	
		end = form.end.data	
		transaction = MemberPayment.query.filter(MemberPayment.date.between(start,end)).filter(MemberPayment.owner == name).all()	
		return render_template("user/marketing_stats.html",transaction=transaction,user=user,form=form)	
	return render_template("user/marketing_stats.html",transaction=transaction,user=user,form=form)





############################## Member Function ###############################
@app.route("/dashboard/add-member",methods=["GET","POST"])
@login_required
def AddMember():
	form = AddMemberForm()
	if form.validate_on_submit():
		today = datetime.today()
		select = form.paket.data
		hass = generate_password_hash(form.password.data,method="sha256")		
		check_user = User.query.filter_by(plat=form.plat.data).all()
		if len(check_user) > 0 :
			flash("Plat telah terdaftar","danger")
		else :	
			if select == "paket1":
				renew = today + timedelta(days=180) 
				user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="pending",date=today,renew=renew,birth=form.birth.data,member="nonregular",paket="paket1",marketing=current_user.username,treatment="Cuci Non Lift")
				db.session.add(user)
				db.session.commit()

				#input si transaksi marketing 
				marketing = MemberPayment(amount=1000000,date=today,owner=current_user.username)
				db.session.add(marketing)
				db.session.commit()
				if current_user.role == "marketing":					
					flash("member berhasil di tambah","success")
					return redirect(url_for("AdminDashboard"))
				else :
					flash("member berhasil di tambah","success")
					return redirect(url_for("AdminDashboard"))
			elif select == "paket2":
				renew = today + timedelta(days=90) 
				user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="pending",date=today,renew=renew,birth=form.birth.data,member="regular",paket="paket2",marketing=current_user.username,treatment="Cuci + lift + Vacum")
				db.session.add(user)
				db.session.commit()

				#input si transaksi marketing 
				marketing = MemberPayment(amount=1500000,date=today,owner=current_user.username)
				db.session.add(marketing)
				db.session.commit()

				if current_user.role == "marketing":					
					flash("member berhasil di tambah","success")
					return redirect(url_for("AdminDashboard"))
				else :
					flash("member berhasil di tambah","success")
					return redirect(url_for("AdminDashboard"))				
			else :
				renew = today + timedelta(days=180) 
				user = User(username=form.username.data,email=form.email.data,password=hass,role="member",phone=form.phone.data,mobil=form.mobil.data,plat=form.plat.data,status="pending",date=today,renew=renew,birth=form.birth.data,member="vip",paket="paket3",marketing=current_user.username,treatment="Cuci + lift + Vacum")
				db.session.add(user)
				db.session.commit()

				#input si transaksi marketing 
				marketing = MemberPayment(amount=3500000,date=today,owner=current_user.username)
				db.session.add(marketing)
				db.session.commit()

				if current_user.role == "marketing":					
					flash("member berhasil di tambah","success")
					return redirect(url_for("AdminDashboard"))
				else :
					flash("member berhasil di tambah","success")
					return redirect(url_for("AdminDashboard"))
				
	return render_template("user/add_member.html",form=form)	



### member berdasarkan lokasi
@app.route("/dashboard/member/location/<string:id>",methods=["GET","POST"])
@login_required
def MemberBasedLocation(id):
	location = Location.query.filter_by(id=id).first()
	members = User.query.filter_by(location=location.location,role="member").all()
	total = len(members)
	return render_template("user/member_based_location.html",members=members,total=total)



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
			return redirect(url_for("AllMarketing"))		
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
		return redirect(url_for("AdminDashboard"))		


############################# Booking Dari Admin ########################
@app.route("/dashboard/admin-booking",methods=["GET","POST"])
@login_required
def AdminBooking():
	return render_template("user/admin_booking.html")



@app.route("/dashboard/admin-booking/regular",methods=["GET","POST"])
@login_required
def AdminBookingRegular():	
	if current_user.role == "superuser":
		form = YudiBookingRegularForm()
		if form.validate_on_submit():							
			today = datetime.today()				
			book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,status="Belum Cuci",role="regular",owner=current_user.id,payment="Belum Lunas",treatment="-",location=form.location.data,price=0)			
			db.session.add(book)
			db.session.commit()			
			flash("Booking berhasil","success")
			return render_template("user/after_booking_regular.html",book=book)
	else:		
		form = BookingForm()
		if form.validate_on_submit():			
			today = datetime.today()					
			book = Book(name=form.name.data,email=form.email.data,phone=form.phone.data,date=today,mobil=form.mobil.data,plat=form.plat.data,status="Belum Cuci",role="regular",owner=current_user.id,location=current_user.location,payment="Belum Lunas",treatment="-",price=0)
			db.session.add(book)
			db.session.commit()
			flash("Booking berhasil","success")
			return render_template("user/after_booking_regular.html",book=book)
	return render_template("user/admin_booking_regular.html",form=form)	



@app.route("/dashboard/admin-booking/member",methods=["GET","POST"])
@login_required
def AdminBookingMember():
	if current_user.role == "superuser":
		form = YudiBookingMemberForm()
		if form.validate_on_submit():	
			member = User.query.filter_by(plat=form.plat.data).first()			
			if member :
				book = Book.query.filter(Book.owner == member.id,Book.status != "out").all()
				today = datetime.today()
				if member.renew == today or today > member.renew :
					flash("Masa berlaku membership telah habis,silakan di perpanjang","danger")	
				elif member.status == "pending" :
					flash("Akun dalam masa pending","danger")
				elif len(book) > 0 :	
					flash("Member telah melakukan booking,tidak bisa booking lebih dari satu","danger")	
				else :																		
					book = Book(name=member.username,email=member.email,phone=member.phone,date=today,mobil=member.mobil,plat=member.plat,paket="Tidak Ada",status="Belum Cuci",role=member.member,owner=member.id,location=form.location.data,payment="Belum Lunas",treatment=member.treatment,price=0)
					db.session.add(book)
					db.session.commit()
					flash("Booking berhasil","success")	
					return render_template("user/after_booking.html",member=member,book=book) 		
			flash("Tidak ada member yang terdaftar atas Plat tersebut","danger")				
			
	else :
		form = BookingMemberForm()
		if form.validate_on_submit():		
			member = User.query.filter_by(plat=form.plat.data).first()			
			if member :
				book = Book.query.filter(Book.owner == member.id,Book.status != "out").all()
				today = datetime.today()
				if member.renew == today or today > member.renew :
					flash("Masa berlaku membership telah habis,silakan di perpanjang","danger")	
				elif member.status == "pending" :
					flash("Akun dalam masa pending","danger")
				elif len(book) > 0 :	
					flash("Member telah melakukan booking,tidak bisa booking lebih dari satu","danger")	
				else :																		
					book = Book(name=member.username,email=member.email,phone=member.phone,date=today,mobil=member.mobil,plat=member.plat,paket="Tidak Ada",status="Belum Cuci",role=member.member,owner=member.id,location=current_user.location,payment="Belum Lunas",treatment=member.treatment,price=0)
					db.session.add(book)
					db.session.commit()
					flash("Booking berhasil","success")	
					return render_template("user/after_booking.html",member=member,book=book) 		
			flash("Tidak ada member yang terdaftar atas Plat tersebut","danger")			
		
					
	return render_template("user/admin_booking_form.html",form=form)	



@app.route("/dashboard/test/add-treatment/<string:id>",methods=["GET","POST"])
@login_required
def TestAddTreatment(id):
	book = Book.query.filter_by(id=id).first()
	user = User.query.filter_by(id=book.owner).first()	
	paketsaya = BookingPaket.query.filter_by(book_id=book.id).all()
	if user.paket == "paket1" or user.paket == "paket2" : 	
		status = "regular" 
		pakets = Paket.query.filter_by(status=status).all()
		return render_template("paket/add-treatment.html",book=book,pakets=pakets,paketsaya=paketsaya,status=status)
	elif user.paket == "paket3":
		status = "vip"
		pakets = Paket.query.filter_by(status=status).all()
		return render_template("paket/add-treatment.html",book=book,pakets=pakets,paketsaya=paketsaya,status=status)			
	else :		 	 
		status = "umum"
		pakets = Paket.query.filter_by(status=status).all()
		return render_template("paket/add-treatment.html",book=book,pakets=pakets,paketsaya=paketsaya,status=status)	
		
	


@app.route("/dashboard/test/insert-treatment/<string:id>/<string:status>/<string:name>",methods=["GET","POST"])
@login_required
def TestIntsertTreatment(id,status,name):	 
	book = Book.query.filter_by(id=id).first()
	id = book.id
	paket = Paket.query.filter_by(name=name,status=status).first()
	check_book = BookingPaket.query.filter(BookingPaket.book_id == book.id,BookingPaket.paket_id == paket.id ).all()
	if len(check_book) > 0 :
		flash("Anda Tidak Bisa Memilih Treatment Yang Sama","danger")
		return redirect(url_for("TestAddTreatment",id=id))
	else :	
		booking = BookingPaket(book_id=book.id,paket_id=paket.id,paket_name=paket.name,paket_price=paket.price)
		db.session.add(booking)
		db.session.commit()

		book.price = book.price + paket.price
		db.session.commit()
		flash("Tambahan Treatment Berhasil Di Tambah","success")
		return redirect(url_for("TestAddTreatment",id=id))





			

###################################### Member route ############################
@app.route("/dashboard/booking",methods=["GET","POST"])
@login_required
def Booking():	
	today = datetime.today()
	check_book = Book.query.filter(Book.owner == current_user.id,Book.status != "out").all()
	if today > current_user.renew and current_user.status == "pending":
		return redirect(url_for("PaymentInfo"))			
	else :
		form = UserBookingForm()
		if form.validate_on_submit():
			today = datetime.today()
			user = current_user	 
			if len(check_book) > 0 :
				flash("Anda tidak bisa booking lebih dari satu sekaligus","danger")	
			else :				
				book = Book(name=user.username,email=user.email,phone=user.phone,date=today,mobil=user.mobil,plat=user.plat,status="Dalam Perjalanan",role=user.member,owner=user.id,location=form.location.data,payment="Belum Lunas",treatment=user.treatment,price=0)
				db.session.add(book)
				db.session.commit()		
				flash("Booking berhasil","success")
				member = current_user
				return render_template("user/after_booking.html",book=book)	
					
	return render_template("user/booking.html",form=form)	










###############################################################
@app.route("/dashboard/location/antrean",methods=["GET","POST"])
@login_required
def AntreanLocation():
	locations = Location.query.all()
	userlocations = Location.query.filter_by(location=current_user.location).all() 
	return render_template("user/antrean_location.html",locations=locations,userlocations=userlocations)



@app.route("/dashboard/antrean/<string:id>",methods=["GET","POST"])
@login_required
def Antrean(id):
	location = Location.query.filter_by(id=id).first()
	nama = location.location	
	antrean = Book.query.filter(Book.location == nama,Book.status != "Out",Book.role != "nonregular").order_by(Book.role.desc()).all()
	nonregulars = Book.query.filter(Book.location == nama, Book.status != "Out", Book.role == "nonregular").order_by(Book.role.desc()).all()
	total = len(antrean)
	jumlah = len(nonregulars)
	return render_template("antrean/antrean.html",antrean=antrean,total=total,nonregulars=nonregulars,jumlah=jumlah)



@app.route("/dashboard/detail/antrean/<string:id>",methods=["GET","POST"])
@login_required
def DetailAntrean(id):
	book = Book.query.filter_by(id=id).first()
	pakets = BookingPaket.query.filter_by(book_id=book.id).all()
	return render_template("antrean/detail_booking.html",book=book,pakets=pakets)




@app.route("/dashboard/edit-antrean/<string:id>",methods=["GET","POST"])
@login_required
def EditAntrean(id):	
	antre = Book.query.filter_by(id=id).first()
	location = Location.query.filter_by(location=antre.location).first()
	id = location.id 
	if current_user.role == "sa":
		form = BookingStatusFormSa()
	else :	
		form = BookingStatusForm()
	form.status.data = antre.status	
	if form.validate_on_submit():
		antre.status = request.form["status"]
		db.session.commit()
		flash("Status berhasil di update","success")
		return redirect(url_for("Antrean",id=id))
	return render_template("user/edit_antrean.html",form=form)	



@app.route("/dashboard/cancel-antrean/<string:id>",methods=["GET","POST"])
@login_required
def CancelAntrean(id):
	book = Book.query.filter_by(id=id).first()
	location = Location.query.filter_by(location=book.location).first()
	id=location.id
	if book.status != "Dalam Perjalanan" or book.status != "Belum Cuci":
		db.session.delete(book)
		db.session.commit()
		flash("Booking berhasil di batalkan","success")
		return redirect(url_for("Antrean",id=id))
	else:
		flash("Booking tidak bisa dibatalkan","danger")
		return redirect(url_for("Antrean",id=id))
		



@app.route("/dashboard/delete-antrean",methods=["GET","POST"])
@login_required
def DeleteAllBooking():
	form = DeleteAntreanForm()
	if form.validate_on_submit():
		books = Book.query.filter(Book.status != "Out").update({Book.status : "Out" })	
		db.session.commit()
		flash("Antrean berhasil di hapus","success")
		return redirect(url_for("AntreanLocation"))
	return render_template("user/delete_antrean.html",form=form)	
















########################################## Package #####################################

#jalu permbuatan ke member atau regular
@app.route("/dashboard/all-package",methods=["GET","POST"])
@login_required
def PilihPackage():
	return render_template("user/pilih_paket.html")


#untuk member
@app.route("/dashboard/add-package/<string:status>",methods=["GET","POST"])
@login_required
def AddPackage(status):
	form = AddPackageForm()
	if form.validate_on_submit():
		if status == "regular" :
			paket = Paket(name=form.name.data,price=form.price.data,status="regular")
			db.session.add(paket)
			db.session.commit()
			flash("Paket berhasil di tambahkan","success")
			return redirect(url_for("AllPackage",status=status))
		elif status == "vip" :
			paket = Paket(name=form.name.data,price=form.price.data,status="vip")
			db.session.add(paket)
			db.session.commit()
			flash("Paket berhasil di tambahkan","success")
			return redirect(url_for("AllPackage",status=status))
		else :
			paket = Paket(name=form.name.data,price=form.price.data,status="umum")
			db.session.add(paket)
			db.session.commit()
			flash("Paket berhasil di tambahkan","success")
			return redirect(url_for("AllPackage",status=status))		
	 	
	return render_template("user/add_package.html",form=form,status=status) 	


@app.route("/dashboard/package/<string:status>",methods=["GET","POST"])
@login_required
def AllPackage(status):
	pakets = Paket.query.filter_by(status=status).all()
	return render_template("user/package.html",pakets=pakets,status=status)

@app.route("/dashboard/edit-package/<string:status>/<string:id>",methods=["GET","POST"])
@login_required
def EditPackage(status,id):
	paket = Paket.query.filter_by(id=id,status=status).first()
	form = AddPackageForm()
	form.name.data = paket.name
	form.price.data = paket.price 
	if form.validate_on_submit():
		paket.name = request.form["name"]
		paket.price = request.form["price"]
		db.session.commit()
		flash("Paket Berhasil Di Edit","success")
		return redirect(url_for("AllPackage",status=status))
	return render_template("user/add_package.html",form=form,status=status)	


@app.route("/dashboard/delete-package/<string:status>/<string:id>",methods=["GET","POST"])
@login_required
def DeletePackage(status,id):
	paket = Paket.query.filter_by(id=id,status=status).first()
	form = SubmitForm()
	if form.validate_on_submit():
		db.session.delete(paket)
		db.session.commit()
		flash("Paket Berhasil Di Hapus","success")
		return redirect(url_for("AllPackage",status=status))
	return render_template("paket/confirm_delete.html",form=form)	




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
	invoices = Book.query.filter_by(location=locname,payment="Belum Lunas").order_by(Book.date.desc()).all()
	userinvoice = Book.query.filter_by(owner=current_user.id).all()
	return render_template("user/all_invoice.html",invoices=invoices,userinvoice=userinvoice,locations=locations)	


@app.route("/dashboard/location/invoice/lunas/<string:id>",methods=["GET","POST"])
@login_required
def AllInvoiceLunas(id):
	locations = Location.query.filter_by(id=id).first()
	locname = locations.location
	invoices = Book.query.filter(Book.location==locname,Book.payment=="Lunas").order_by(Book.date.desc()).all()
	return render_template("user/all_invoice_lunas.html",invoices=invoices,locations=locations)


@app.route("/dashboard/location/invoice/history/<string:id>",methods=["GET","POST"])
@login_required
def AllInvoiceHistory(id):
	locations = Location.query.filter_by(id=id).first()
	locname = locations.location
	invoices = Book.query.filter(Book.location==locname,Book.payment=="History").order_by(Book.date.desc()).all()
	form = AccountingSearchForm()
	if form.validate_on_submit():
		end = form.end.data 
		start = form.start.data
		invoices = Book.query.filter(Book.date.between(start,end)).filter(Book.payment != "Belum Lunas").all()
		return render_template("user/all_invoice_history.html",invoices=invoices,locations=locations,form=form)
	return render_template("user/all_invoice_history.html",invoices=invoices,locations=locations,form=form)






@app.route("/dashboard/invoice/<string:id>",methods=["GET","POST"])
@login_required
def UserInvoice(id):
	invoice = Book.query.filter_by(id=id).first()
	user = User.query.filter_by(id=invoice.owner).first()
	membership = user.renew
	pakets = BookingPaket.query.filter_by(book_id=invoice.id).all()	
	if current_user.role == "cashier":
		if invoice.payment == "Belum Lunas":
			today = datetime.today()
			location = invoice.location
			invoice.payment = "Lunas"		
			total = invoice.price
			result = []
			pakets = BookingPaket.query.filter_by(book_id=invoice.id).all()
			for x in pakets :
				result.append(x.paket_name)
			harga = "{:,}".format(total).replace(",",".") 													
			trans = Accounting(description="Pembayaran dari customer",amount=total,date=today,location=location,status="Income",cashier=current_user.username,pakets=result,customer=invoice.plat,member=invoice.treatment)
			db.session.add(trans)
			db.session.commit()				
					
			return render_template("paket/invoice.html",invoice=invoice,pakets=pakets,harga=harga,user=user,membership=membership)		
	else :								
		total = invoice.price				
		harga = "{:,}".format(total).replace(",",".") 							
		return render_template("paket/invoice.html",invoice=invoice,pakets=pakets,harga=harga,user=user,membership=membership) 
					



#### invoice member ####
@app.route("/dashboard/invoice",methods=["GET","POST"])
@login_required
def AllMemberInvoice():
	invoices = Book.query.filter_by(owner=current_user.id,payment="Belum Lunas").all()
	return render_template("user/member_invoice.html",invoices=invoices)





@app.route("/dashboard/admin/delete-invoice/<string:id>",methods=["GET","POST"])
@login_required
def DeleteInvoiceByYudi(id):
	if current_user.role == "superuser":
		book = Book.query.filter_by(id=id).first()
		db.session.delete(book)
		db.session.commit()
		flash("Invoice berhasil di hapus","success")
		return redirect(url_for("InvoiceLocation"))
	else :
		return "no access"	

















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









####################### Accounting ###########################

@app.route("/dashboard/add-income",methods=["GET","POST"])
@login_required
def AddIncome():
	if current_user.role == "superuser" or current_user.role == "accountant" :
		form = SuperUserAddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			income = Accounting(description=form.description.data,location=form.location.data,amount=form.amount.data,date=today,status="Income",cashier=current_user.username)
			db.session.add(income)
			db.session.commit()
			flash("Pendapatan berhasil di input","success")
			return redirect(url_for("AdminDashboard"))
	else :
		form = AddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			income = Accounting(description=form.description.data,location=current_user.location,amount=form.amount.data,date=today,status="Income",cashier=current_user.username)
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
			expense = Accounting(description=form.description.data,location=form.location.data,amount=form.amount.data,date=today,status="Expense",cashier=current_user.username)
			db.session.add(expense)
			db.session.commit()
			flash("Pengeluaran berhasil di input","success")
			return redirect(url_for("AdminDashboard"))
	else :	
		form = AddAccountingForm()
		if form.validate_on_submit():
			today = datetime.today()
			expense = Accounting(description=form.description.data,location=current_user.location,amount=form.amount.data,date=today,status="Expense",cashier=current_user.username)
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
	income =  Accounting.query.filter_by(location=name,status="Income").all()	
	expense = Accounting.query.filter_by(location=name,status="Expense").all()	
	form = AccountingSearchForm()
	if form.validate_on_submit():
		start = form.start.data
		end = form.end.data
		return redirect(url_for("TransactionFilter",start=start,end=end,id=id))
	return render_template("user/all_transaction.html",transactions=transactions,form=form,name=name,location=location,income=income,expense=expense)


@app.route("/dashboard/location/transaction/filter/<start>/<end>/<string:id>",methods=["GET","POST"])
@login_required
def TransactionFilter(start,end,id):
	location = Location.query.filter_by(id=id).first()
	name = location.location
	id=location.id
	transactions = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name).all()
	income =  Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name,Accounting.status=="Income").all()
	expense = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name,Accounting.status=="Expense").all()
	form = AccountingSearchForm()
	if form.validate_on_submit():
		start = form.start.data
		end = form.end.data		
		return redirect(url_for("TransactionFilter",start=start,end=end,id=id))
	return render_template("user/all_transaction_filter.html",transactions=transactions,form=form,name=name,location=location,start=start,end=end,income=income,expense=expense)




#printing all transaction
@app.route("/dashboard/location/transaction/print/<string:id>",methods=["GET","POST"])
@login_required
def PrintAllTransaction(id):
	location = Location.query.filter_by(id=id).first()
	name = location.location
	transactions = Accounting.query.filter_by(location=name).all()
	income =  Accounting.query.filter_by(location=name,status="Income").all()	
	expense = Accounting.query.filter_by(location=name,status="Expense").all()	
	return render_template("transaction/print_all.html",transactions=transactions,name=name,income=income,expense=expense)

#printing all transaction after filter
@app.route("/dashboard/location/transaction/print/<start>/<end>/<string:id>",methods=["GET","POST"])
@login_required
def PrintAllFilterTransaction(start,end,id):
	location = Location.query.filter_by(id=id).first()
	name = location.location
	transactions = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name).all()
	income =  Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name,Accounting.status=="Income").all()
	expense = Accounting.query.filter(Accounting.date.between(start,end)).filter(Accounting.location == name,Accounting.status=="Expense").all()
	return render_template("transaction/print_all.html",transactions=transactions,name=name,income=income,expense=expense)











############################### Payment info ######################
@app.route("/dashboard/info-payment")
def PaymentInfo():
	return render_template("user/payment_info.html")



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











if __name__ == "__main__":	
	app.run(debug=True)
