from django import forms
from django.contrib.auth.models import User

from home.models import NewsletterSignup
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = user.first_name + "." +user.last_name
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['email']