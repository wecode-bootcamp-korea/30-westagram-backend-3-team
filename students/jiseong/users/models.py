from django.db import models

class User(models.Model):
    last_name    = models.CharField(max_length=45)
    first_name   = models.CharField(max_length=45)
    email        = models.CharField(max_length=45, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='users'