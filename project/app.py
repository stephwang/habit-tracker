import os
from flask import Flask, render_template, redirect
from flask import request
from flask_pymongo import PyMongo

import controllers.auth as auth

app = Flask(__name__)

MONGO_URL = os.environ.get('MONGODB_URI')

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def user_login():
    s = auth.AuthHandler(request, mongo)
    return render_template('login.html')
    
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup/', methods=['POST'])
def user_signup():
    s = auth.SignupHandler(request, mongo)
    params = s.validate_form()
    if not params:
        return redirect("/")
    else: 
        return render_template('signup.html'
                                , username = params.get('username', '')
                                , email = params.get('email', '')
                                , username_error = params.get('username_error', '')
                                , password_error = params.get('password_error', '')
                                , password_match_error = params.get('password_match_error', '')
                                , email_error = params.get('email_error', '')
                            )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)
