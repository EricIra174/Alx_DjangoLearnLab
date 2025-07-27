from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom User model
class CustomUser(AbstractUser):
    "date_of_birth" = models.DateField(null=True, blank=True)
    "profile_photo" = models.ImageField(upload_to="profile_photos/", null=True, blank=True)

    def __str__(self):
        return self.username


# ✅ Book model
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

    def __str__(self):
        return self.title


# ✅ Sample model with permissions (if needed)
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
        return self.name
