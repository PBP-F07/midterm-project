from landingPage.models import Books
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    year_of_release = models.CharField(max_length=10)

class newWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class addWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.TextField(max_length=200)