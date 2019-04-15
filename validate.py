import re
ALPHANUM = re.compile('[a-zA-Z0-9_.-]')

def validate_username(username):
    username_error = False
    if len(username) > 20 or len(username) < 4:
        username_error = True

    for char in username:
        if ALPHANUM.match(char) is None:
            username_error = True
    return username_error

def validate_password(password):
    password_error = False
    if len(password) > 20 or len(password) <4:
        password_error = True

    for char in password:
        if ALPHANUM.match(char) is None:
            password_error = True
    
    return password_error

def verify_password(password, verify):
    verify_password_error = False
    if password != verify:
        verify_password_error = True
    
    return verify_password_error

def verify_email(email):
    email_error = False
    if len(email) > 0:
        if email.count('@') == 0 or email.count('.') or email.count(' ') > 0:
            email_error = True

    return email_error


        

        

        