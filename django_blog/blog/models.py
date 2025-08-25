from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    def get_book_details(self):
        return {
            "title": self.title,
            "content": self.content,
            "published_date": self.published_date,
            "author": self.author.username,
        }
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
