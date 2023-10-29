from django.forms import ModelForm
from .models import discussion,reply


class CommentForm(ModelForm):
    class Meta:
        model = discussion
        fields = ["comment"]


class ReplyForm(ModelForm):
    class Meta:
        model = reply
        fields = ["replies"]