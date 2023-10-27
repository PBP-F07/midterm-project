from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    year_of_release = models.CharField(max_length=10)
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='borrowed_books', blank=True)
