from flask import render_template, flash, redirect, url_for, session, request
from flask_login import current_user
from burrow512 import app, mysql
from requests_oauthlib import OAuth2Session
from .env.settings import Auth
from urllib2 import HTTPError
import json
from .utils.auth import get_google_auth
import itertools


#golden function that takes a cursor and returns a dictionary list with column names as key
def dictfetchall(cursor):
    desc = cursor.description
    return [dict(itertools.izip([col[0] for col in desc], row)) for row in cursor.fetchall()]


@app.route('/about')
def about():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM faqs ORDER BY pos""")
    res = dictfetchall(cur)
    res.append({'question':"what?", 'answer':"this"}) 
    return render_template("about.html",
            faqs=res,
            title='About')


@app.route('/login')
def login():
    return render_template("todo.html")

    if current_user.is_authenticated:
            return redirect(url_for('index'))

    google = get_google_auth()
    auth_url, state = google.authorization_url(Auth.AUTH_URI, access_type='offline')
    session['oauth_state'] = state
    print(session)
    
    return redirect(auth_url)


@app.route('/gCallback')
def callback():
    if current_user is not None and current_user.is_authenticated:
            return redirect(url_for('index'))
    if 'error' in request.args:
            if request.args.get('error') == 'access_denied':
                    return 'you denied access'
            return 'Error encountered'
    if 'code' not in request.args and 'state' not in request.args:
            return redirect(url_for('login'))
    else:
            print(session)
            google = get_google_auth(state=session['oauth_state'])
            try:
                    token = google.fetch_token(
                            Auth.TOKEN_URI,
                            client_secret=Auth.CLIENT_SECRET,
                            authorization_response=request.url)
            except HTTPError:
                    return "HTTPERROR occured"
            google = get_google_auth(token=token)
            resp = google.get(Auth.USER_INFO)
            if resp.status_code == 200:
                    user_data = resp.json()
                    email = user_data['email']
                    user = User.query.filter_by(email=email).first()
                    if user is None:
                            user = User()
                            user.email = email
                    user.name = user_data['name']
                    user.tokens = json.dumps(token)
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect(url_for('index'))
            return "Could not fetch your info"


@app.route('/')
@app.route('/index')
def index():
    res = render_template("index.html",
                    title='512\'s burrow',
                    message = "Hello world")

    return res



