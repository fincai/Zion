from django.db import models
from zion.signin.models import User
from zion.articles.models import Article


class Comment(models.Model):
    post_date = models.DateTimeField()
    poster = models.ForeignKey(User)
    article = models.ForeignKey(Article) 
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'comment'
    
    
