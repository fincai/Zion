from django.db import models
from zion.articles.models import Article

class Tag(models.Model):
    keyword = models.CharField(max_length=255)
    articles = models.ManyToManyField(Article)
    article_count = models.PositiveIntegerField(default=0)
    proposed_date = models.DateTimeField()

    class Meta:
        db_table = 'tag'
    
