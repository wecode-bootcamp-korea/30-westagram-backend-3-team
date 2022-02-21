import re

def vaildate_email(email):
    return re.match('\w+@\w+\.\w', email)
    
def vaildate_password(password):
    return re.match('(?=.*[a-zA-Z])(?=.*\d)(?=.*[?!@#$%^&*-]).{8,}', password)