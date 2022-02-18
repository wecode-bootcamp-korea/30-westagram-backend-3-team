import re

def email_validation(email):
    email_regex = re.compile(r"^([0-9a-zA-Z]?[+-_.]?[0-9a-zA-Z])+@[a-zA_Z-]+[.][a-zA_Z-]+$")

    if not re.match(email_regex, email):
        return False

def password_validation(password):
    password_regex = re.compile("^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}")
    if not re.match(password_regex, password):
        return False
