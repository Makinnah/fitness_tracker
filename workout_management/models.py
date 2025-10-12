from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('Running', 'Running'),
        ('Cycling', 'Cycling'),
        ('Weightlifting', 'Weightlifting'),
        ('Swimming', 'Swimming'),
        ('Yoga', 'Yoga'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    distance = models.FloatField(blank=True, null=True, help_text="Distance in km or miles")
    calories_burned = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"
