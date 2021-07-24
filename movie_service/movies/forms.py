from django import forms
from .models import Movies, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        field=['comment','rate']
        