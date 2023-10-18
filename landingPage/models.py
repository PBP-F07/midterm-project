from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    year_of_release = models.CharField(max_length=10)