from django.db import models

from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=30)
    email        = models.CharField(max_length=100)
    password     = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'
