from django.db import models

# Create your models here.
class User(models.Model):
    first_name   = models.CharField(max_length=10)
    last_name    = models.CharField(max_length=10)
    email        = models.EmailField(max_length=50, unique=True)
    password     = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True)

    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

class Follow(models.Model):
    following = models.ForeignKey('User', on_delete=models.CASCADE, related_name="following")
    followed  = models.ForeignKey('User', on_delete=models.CASCADE, related_name="followed")
    # following = models.ForeignKey('User', on_delete=models.CASCADE)
    # followed  = models.ForeignKey('User', on_delete=models.CASCADE)

    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "follows"