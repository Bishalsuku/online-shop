from django import forms
from django.contrib.auth.models import User


class Signup_Form(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Last Name"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Email Address"})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Shipping Address"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "password", "email", "username", "address")
        labels = {"first_name": "First Name", "last_name": "Last Name"}

    def clean(self):
        cleaned_data = super(Signup_Form, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password doesnot match")