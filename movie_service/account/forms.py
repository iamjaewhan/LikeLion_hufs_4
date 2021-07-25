from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2', 'email']
        labels = {
            'username': 'ID',
            'password2': 'password verification',
        }


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        # help_texts = {
        #     'username' : None,
        #     'email' : None,
        #     'password2' : None,
        # }

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
