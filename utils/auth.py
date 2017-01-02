from requests_oauthlib import OAuth2Session
from ..config import Auth
from urllib2 import HTTPError


def get_google_auth(state=None, token=None):
	if token:
		return OAuth2Session(Auth.CLIENT_ID, token=token)
	if state:
		return OAuth2Session(
			Auth.CLIENT_ID,
			state=state,
			redirect_uri=Auth.REDIRECT_URI)
	oauth = OAuth2Session(
		Auth.CLIENT_ID,
		redirect_uri=Auth.REDIRECT_URI,
		scope=Auth.SCOPE)
	return oauth
