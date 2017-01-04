
from .env.settings import mysqluser, mysqlpwd, secret_key
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	WTF_CSRF_ENABLED = True
	SECRET_KEY = secret_key
        MYSQL_USER = mysqluser
        MYSQL_PASSWORD = mysqlpwd
        MYSQL_DB = "512burrow"
        MYSQL_HOST = "localhost"

class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

config = {
	"dev": DevConfig
}

