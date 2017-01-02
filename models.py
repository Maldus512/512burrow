from burrow512 import db, login_manager
from flask_login import UserMixin
import datetime


@login_manager.user_loader
def get_user(ident):
	return User.query.get(int(ident))


class User(db.Model, UserMixin):
	__tablename__ = "users"
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True, nullable=False)
	name = db.Column(db.String(100), nullable=True)
	active = db.Column(db.Boolean, default=False)
	tokens = db.Column(db.Text)
	created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
