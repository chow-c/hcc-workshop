from django import forms
from django.contrib.auth.models import User

from home.models import NewsletterSignup
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        temp_username = user.first_name.lower() + "." +user.last_name.lower()

        if User.objects.filter(username__iexact=temp_username).exists():
            temp_username = temp_username + str(User.objects.filter(username__startswith=temp_username).count()+1)
            user.username = temp_username
        else:
            user.username = temp_username

        if commit:
            user.save()
        return user

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['email']