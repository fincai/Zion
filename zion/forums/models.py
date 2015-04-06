from django.db import models
from zion.signin.models import User

class Forum(models.Model):
    topic = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    articles = models.PositiveIntegerField(default=0)
    closed = models.BooleanField(default=False)
    last_author = models.ForeignKey(User, null=True)
    last_postdate = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'forum'
        
    def __unicode__(self):
        return '{0}-{1}'.format(self.topic, self.name)
        
