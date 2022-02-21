from django.db import models

# Create your models here.
class User(models.Model):
    username        = models.CharField(max_length=30)
    email           = models.EmailField(max_length=40, unique=True, null=True)
    password        = models.CharField(max_length=150)
    phone_number    = models.CharField(max_length=16) 
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'