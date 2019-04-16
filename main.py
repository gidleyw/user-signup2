from flask import Flask, request, redirect
import cgi
import os
import jinja2
from validate import validate_password, validate_username, verify_email, verify_password

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route('/', methods=['POST'])
def validate():
    template = jinja_env.get_template('form.html')
    username = request.form['username']
    password = request.form['password']
    verify   = request.form['verify']
    email    = request.form['email']

    username_error        = ''
    password_error        = ''
    verify_password_error = ''
    email_error           = ''
    errors = 0

    if validate_username(username):
        username_error = "Username needs to be between 3 and 20 characters"
        errors += 1
    else:
        username_error = ''
    
    if validate_password(password):
        password_error = "That's not a valid password"
        errors += 1
    else:
        password_error = ''

    if verify_password(password,verify):
        verify_password_error = "Passwords don't match"
        errors += 1
    else:
        verify_password_error = ''

    if verify_email(email):
        email_error = "That's not a valid email"
        errors += 1
    else:
        email_error = ''

    if errors == 0:
        user = username
        return redirect('/hello?user={0}'.format(user))
    else:
        return template.render(user=username, email_address=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route('/hello')

def hello():
    user = request.args.get('user')
    template = jinja_env.get_template('validation_return.html')
    return template.render(user=user)




app.run()