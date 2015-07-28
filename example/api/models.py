from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='followees', symmetrical=False)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
    	return "%s" % self.title


class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")

    def __unicode__(self):
    	return "%s" % self.image
