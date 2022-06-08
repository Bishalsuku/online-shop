from django import forms
from django.contrib.auth.models import User


class login_form(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    class Meta:
        model = User
        fields = ("username", "password")
