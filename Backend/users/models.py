from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=100, blank=True)
    year = models.CharField(
        max_length=20,
        choices=[
            ('freshman', 'Freshman'),
            ('sophomore', 'Sophomore'),
            ('junior', 'Junior'),
            ('senior', 'Senior'),
            ('graduate', 'Graduate'),
        ],
        blank=True
    )
    interests = models.JSONField(default=list, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.username
