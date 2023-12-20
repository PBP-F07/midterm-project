from django.db import models
from django.contrib.auth.models import User
from landingPage.models import Books

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username
