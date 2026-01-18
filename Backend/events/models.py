from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('career', 'Career'),
        ('social', 'Social'),
        ('sports', 'Sports'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='social')
    date = models.DateField()
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    interested_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
