from django.db import models

# Create your models here.
class mytask(models.Model):
    task = models.TextField()
    location = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)