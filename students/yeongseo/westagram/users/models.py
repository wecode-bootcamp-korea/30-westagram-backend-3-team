from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=16) #+82등 국가번호 붙는 경우 감안하여 char로 필드 지정
    class Meta:
        db_table = 'users'