from app import db,Book
from flask_sqlalchemy import SQLAlchemy 

def InvoiceHistory():
	book = Book.query.filter(Book.payment == "Lunas").update({Book.payment : "History"})
	db.session.commit()
	

