from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UserFormChangeInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']  # Corrigido aqui