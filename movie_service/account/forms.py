from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2', 'email']
        labels={
            'username':'ID',
            'passowrd2':'password verification',
        }