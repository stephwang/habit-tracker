from lib import utils
import Cookie

class AuthHandler():

    def set_secure_cookie(self, name, val):
        cookie_val = utils.make_secure_val(val)
        c = Cookie.SimpleCookie()
        c[name] = cookie_val

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and utils.check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        c = Cookie.SimpleCookie()
        c['user_id'] = ''

    # def initialize(self):
    #    uid = self.read_secure_cookie('user_id')
    #    self.user = uid and User.by_id(int(uid))

class LoginHandler(AuthHandler):
    def __init__(self, request, mongo):
        self.username = request.form.get('username')
        self.password = request.form.get('password')
        self.mongo = mongo  
    
    def validate_login(self):
        u = self.mongo.db.users.find_one({ 'username': self.username })
        if u and utils.valid_pw(self.username, self.password, u.password):
            self.login(u)
            return 0
        else:
            return 1
    
class SignupHandler(AuthHandler):

    def __init__(self, request, mongo):
        self.username = request.form.get('username')
        self.password = request.form.get('password')
        self.verify = request.form.get('verify')
        self.email = request.form.get('email')
        self.mongo = mongo
    
    def validate_form(self):
        # object for tracking form errors
        num_errors = 0
        params = { 'username': self.username, 'email': self.email }
        
        # form input validation
        if not utils.valid_username(self.username):
            params['username_error'] = "Please enter a valid username."
            num_errors += 1
        if not utils.valid_password(self.password):
            params['password_error'] = "Please enter a valid password."
            num_errors += 1
        if not utils.password_match(self.password, self.verify):
            params['password_match_error'] = "Passwords do not match."
            num_errors += 1
        if self.email and not utils.valid_email(self.email):
            params['email_error'] = "Please enter a valid email."
            num_errors += 1
            
        # check if user exists already
        u = self.mongo.db.users.find_one({'username': self.username})
        if u:
            params['username_error'] = "User already exists"
            num_errors += 1
        
        if num_errors > 0:
            return params
        else:
            # hash password
            pw_hash = utils.make_pw_hash(self.username, self.password)
            # add user to db
            u = self.mongo.db.users.insert_one({
                 "username": self.username,
                 "password": pw_hash,
                 "email": self.email,
            })
            
            # add cookie
            self.login(u)
            
            return False