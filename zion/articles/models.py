from django.db import models
from zion.signin.models import User
from zion.forums.models import Forum

class Article(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    text = models.TextField()
    post_date = models.DateTimeField()
    last_modify = models.DateTimeField(null=True, blank=True)
    score = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    closed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'article'
    
    
    
    
