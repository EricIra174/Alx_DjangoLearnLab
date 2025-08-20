from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    attendees = models.ManyToManyField(
        CustomUser,
        related_name='attending_events',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    def clean(self):
        # Prevent creating events in the past
        if self.date_time and self.date_time < timezone.now():
            raise ValidationError("Event date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def available_slots(self):
        return self.capacity - self.attendees.count()

    @property
    def is_full(self):
        return self.attendees.count() >= self.capacity


class EventRegistration(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='event_registrations'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    registered_at = models.DateTimeField(auto_now_add=True)
    is_waitlisted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'event')
        ordering = ['registered_at']

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
