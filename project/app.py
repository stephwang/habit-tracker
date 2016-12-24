import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) # set to 5000 for heroku, 8080 when working in cloud 9  
    app.run(host='0.0.0.0', port=port, debug=True)
