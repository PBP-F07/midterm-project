from django.forms import ModelForm
from user_profile_page.models import Member
from django import forms


class MemberForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))
    class Meta:
        model = Member
        fields = ['bio']