from django.db import models
from django.forms import PasswordInput

#이름 이메일 비번 연락처

class UserData(models.Model):
    name        = models.CharField(max_length=45)
    email       = models.CharField(max_length=45)
    password    = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=45)
    
    class Meta:
        db_table='userdatas'