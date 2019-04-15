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
        username_error = "Usernames required to be between 3-20 alphanumeric characters"
        errors += 1
    else:
        username_error = ''
    
    if validate_password(password):
        password_error = "Passwords required to be between 3-20 alphanumeric characters"
        errors += 1
    else:
        password_error = ''

    if verify_password(password,verify):
        verify_password_error = "Passwords do not match"
        errors += 1
    else:
        verify_password_error = ''

    if verify_email(email):
        email_error = "Invalid Email address input"
        errors += 1
    else:
        email_error = ''

    if errors > 0:
        return redirect('/hello')
    else:
        return template.render(username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route('/hello')

def hello():
    return "<h1>SUCCESS</h1>"
    """user = request.args.get(username)
    template = jinja_env.get_template('validation_return.html')
    return template.render(user=username)"""




app.run()