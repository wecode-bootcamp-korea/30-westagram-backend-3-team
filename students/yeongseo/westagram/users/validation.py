import re

def email_validate(email):
    email_regex = '^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email) == None:
        return False

def password_validate(password):
    password_regex = "(?=.*[A-Za-z])(?=.*\d)(?=.*[$@!%*#?&])[A-Za-z\d$@!%*#?&]{8,}"
    if re.match(password_regex,password) == None:
        return False