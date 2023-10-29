from django.forms import ModelForm
from wishlist_page.models import newWishlist

class BookForm(ModelForm):
    class Meta:
        model = newWishlist
        fields = ["title", "author"]