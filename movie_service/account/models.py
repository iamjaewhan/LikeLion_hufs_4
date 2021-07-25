from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.forms import UserCreationForm
# from django import forms

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
    
#     def __init__(self, *args, **kwargs):
#         super(UserCreationForm, self).__init__(*args, **kwargs)
        
#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
# print UserCreationForm()