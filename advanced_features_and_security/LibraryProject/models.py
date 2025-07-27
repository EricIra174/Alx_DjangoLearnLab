from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
        
    class YourModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view", "Can view item"),
            ("can_create", "Can create item"),
            ("can_edit", "Can edit item"),
            ("can_delete", "Can delete item"),
        ]


    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
