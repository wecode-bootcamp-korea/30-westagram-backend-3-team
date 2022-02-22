from django.db import models

class Posting(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    img_url    = models.URLField(max_length=300)
    content    = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'postings'

class Comment(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post       = models.ForeignKey('Posting', on_delete=models.CASCADE)
    content    = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

class Like(models.Model):
    user       = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post       = models.ForeignKey('Posting', on_delete=models.CASCADE)

    class Meta:
        db_table = 'like'     