import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from zion.settings import AVATAR_ROOT


class User(AbstractUser):
    gender = models.BooleanField(default=False)
    avatar_image = models.CharField(max_length=255, null=True, blank=True)
    _avatar_crop = models.CharField(max_length=255, null=True, blank=True, db_column='avatar_crop')
    avatar_original = models.CharField(max_length=255, null=True, blank=True)
    avatar_temp = models.CharField(max_length=255, null=True, blank=True)
    avatar_type = models.CharField(max_length=10, null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    articles = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    follower  = models.PositiveIntegerField(default=0)
    follows = models.ManyToManyField('self', related_name='follows_set', symmetrical=False)
    fans = models.ManyToManyField('self', related_name='fans_set', symmetrical=False)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=255, null=True, blank=True)
    
    def delete_avatar_temp(self):
        if self.avatar_temp:
            try:
                abspath = AVATAR_ROOT + self.avatar_temp
                if os.path.isfile(abspath):
                    os.remove(abspath)
            except Exception:
                pass
        self.avatar_temp = None

    def delete_avatar_image(self):
        if self.avatar_image:
            try:
                abspath = AVATAR_ROOT + self.avatar_image
                if os.path.isfile(abspath):
                    os.remove(abspath)
                # Delete avatar of different sizes
                for size in (100, 80, 60, 40, 24):
                    path = AVATAR_ROOT + str(size) + '_' + self.avatar_image
                    if os.path.isfile(path):
                        os.remove(path)
            except Exception:
                pass
        self.avatar_image = None
        self.delete_avatar_temp()



    class Meta:
        db_table = 'user'
    
