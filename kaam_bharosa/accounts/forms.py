from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

from django.core.validators import MinLengthValidator

class SignupForm(forms.ModelForm):
    phone = forms.CharField()
    role = forms.ChoiceField(choices=UserProfile.ROLE_CHOICES)
    profile_photo = forms.ImageField(required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[MinLengthValidator(6)],
        help_text="Password must be at least 6 characters long"
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)
