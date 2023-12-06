from django.forms import ModelForm
from wishlist_page.models import addWishlist, Mood
from django import forms

class BookForm(ModelForm):
    class Meta:
        model = addWishlist
        fields = ["title", "author"]

class MoodForm(ModelForm):
    mood = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
    class Meta:
        model = Mood
        fields = ['mood']