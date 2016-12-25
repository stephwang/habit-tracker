import os
from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

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
    
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signup/', methods=['POST'])
def user_signup():
    username = request.form.get('username')
    password = request.form.get('password')
    verify = request.form.get('verify')
    email = request.form.get('email')
    mongo.db.users.insert_one(
        {
            "username": username,
            "password": password,
            "email": email,
        })
    return render_template('signup.html'
                            , username = username
                            , password = password
                            , verify = verify
                            , email = email)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)
