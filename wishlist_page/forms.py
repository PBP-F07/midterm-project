from django.forms import ModelForm
from wishlist_page.models import Notes

class BookForm(ModelForm):
    class Meta:
        model = Notes
        fields = ["notes"]