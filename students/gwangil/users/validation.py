import re

def email_validation(email):
    EMAIL_REGEX = re.match(r"^([0-9a-zA-Z]?[+-_.]?[0-9a-zA-Z])+@[a-zA_Z-]+[.][a-zA_Z-]+$", email)
    return EMAIL_REGEX

def password_validation(password):
    PASSWORD_REGEX = re.match(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}", password)
    return PASSWORD_REGEX