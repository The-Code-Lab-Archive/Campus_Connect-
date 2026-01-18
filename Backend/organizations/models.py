from django.db import models

class Organization(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('career', 'Career'),
        ('social', 'Social'),
        ('sports', 'Sports'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='social')
    description = models.TextField(blank=True)
    members = models.IntegerField(default=0)
    email = models.EmailField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
