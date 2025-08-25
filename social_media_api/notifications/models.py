from django.db import models
from django.conf import settings

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actor_notifications')
    verb = models.CharField(max_length=255)
    target = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='notifications', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Notification for {self.recipient.username} by {self.actor.username}: {self.verb}'