from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=10)
    email        = models.CharField(max_length=50)
    password     = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = "users"