from django.db import models

class Forum(models.Model):
    topic = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    articles = models.PositiveIntegerField(default=0)
    closed = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'forum'
        
    def __unicode__(self):
        return '{0}-{1}'.format(self.topic, self.name)
        
