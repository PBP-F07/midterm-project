from django.forms import ModelForm
from wishlist_page.models import WishlistItem

class BookForm(ModelForm):
    class Meta:
        model = WishlistItem

        from landingPage.models import Books
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class WishlistItem(models.Model):
    fields = ["user", "title", "author", "description", "image", "year_of_release"]