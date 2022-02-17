from django.db import models
from django.forms import PasswordInput

#이름 이메일 비번 연락처

class User(models.Model):
    last_name    = models.CharField(max_length=45)
    first_name   = models.CharField(max_length=45)
    email        = models.CharField(max_length=45, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45)
    create_at    = models.DateTimeField(auto_now_add=False)
    
    class Meta:
        db_table='users'