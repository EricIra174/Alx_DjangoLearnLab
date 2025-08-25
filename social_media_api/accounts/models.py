from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='Followers', blank=True)
    following = ManyToManyField('self', symmetrical=False, related_name='Following', blank=True)
    def __str__(self):
        return self.username