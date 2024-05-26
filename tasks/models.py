from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    
