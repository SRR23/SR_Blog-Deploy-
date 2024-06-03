from django.db import models
from account.models import User
from post.models import Post

# Create your models here.
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    user=models.ForeignKey(User,related_name='user_review',on_delete=models.CASCADE)
    blog=models.ForeignKey(Post,related_name='blog_review',on_delete=models.CASCADE)
    comment=models.TextField(max_length=250)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)],null=True)
    created_date=models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.comment

class Reply(models.Model):
    user=models.ForeignKey(User,related_name='user_replies',on_delete=models.CASCADE)
    comment=models.ForeignKey(Review,related_name='comment_replies',on_delete=models.CASCADE)
    text=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.text