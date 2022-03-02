from django.db    import models

class Posting(models.Model):
    user      = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="postings")

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "posts"


class Image(models.Model):
    image_url = models.CharField(max_length=200)
    posting   = models.ForeignKey('Posting', on_delete=models.CASCADE, related_name="imgs")

    class Meta:
        db_table = "images"


class Comment(models.Model):
    content   = models.CharField(max_length=500)
    user      = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="comments")
    posting   = models.ForeignKey('Posting', on_delete=models.CASCADE, related_name="comments")

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comments"


class Like(models.Model):
    user      = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="likes")
    posting   = models.ForeignKey('Posting', on_delete=models.CASCADE, related_name="likes")

    # create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "likes"