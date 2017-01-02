from flask import Flask
from flask_mysqldb import MySQL
from burrow512.config import config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config['dev'])
mysql = MySQL(app)

from burrow512 import views#, models
