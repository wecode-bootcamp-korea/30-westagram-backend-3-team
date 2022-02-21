from django.db import models

class User(models.Model):
    username   = models.CharField(max_length=30)
    email      = models.EmailField(max_length=250, unique=True)
    password   = models.CharField(max_length=200)
    contact    = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
