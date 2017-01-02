
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Auth:
	CLIENT_ID = ('333849030987-tjf5ejragjkeao1n9s85msl3e0gmmhuq'
		'.apps.googleusercontent.com')
	CLIENT_SECRET = "IwHmgQ3YdJMZhgEnoFp19vzc"
	#REDIRECT_URI = 'http://localhost:5000/gCallback'
	REDIRECT_URI = 'https://192.168.0.117:5000/gCallback'
	AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
	TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
	USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
	SCOPE = ['profile', 'email']

class Config:
	WTF_CSRF_ENABLED = True
	SECRET_KEY = 'super secret'

class DevConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

config = {
	"dev": DevConfig
}

