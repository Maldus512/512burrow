from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from burrow512.config import config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config['dev'])
#db = SQLAlchemy(app)
#login_manager = LoginManager(app)
#login_manager.login_view = "login"
#login_manager.session_protection = "strong"

from burrow512 import views#, models
