# signup/forms.py
from django import forms
from .models import User
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
    sex = forms.ChoiceField(choices=User.SEX_CHOICES, label="Sex")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'sex', 'age', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data
