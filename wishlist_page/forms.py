from django.forms import ModelForm
from wishlist_page.models import addWishlist

class BookForm(ModelForm):
    class Meta:
        model = addWishlist
        fields = ["title", "author"]