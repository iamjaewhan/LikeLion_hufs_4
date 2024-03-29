from django import forms
from .models import Movies, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment','rate']
        labels={
            'comment':'comment',
            'rate':'rate',
        }