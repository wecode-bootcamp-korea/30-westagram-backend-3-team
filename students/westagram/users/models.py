from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=30)
    email        = models.CharField(max_length=100)
    password     = models.IntegerField(max_length=100)
    phone_number = models.IntegerField(max_length=100)

    class Meta:
        db_table = 'users'
