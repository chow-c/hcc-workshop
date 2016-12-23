from django import forms
from django.contrib.auth.models import User

from home.models import NewsletterSignup
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, HTML
from crispy_forms.bootstrap import Field, Alert

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"].replace(" ","") # Remove all white space
        user.last_name = self.cleaned_data["last_name"].replace(" ","") # Remove all white space
        
        temp_username = user.first_name.lower() + "." +user.last_name.lower()

        if User.objects.filter(username__iexact=temp_username).exists():
            temp_username = temp_username + str(User.objects.filter(username__startswith=temp_username).count()+1)
            user.username = temp_username
        else:
            user.username = temp_username

        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
            super(UserCreateForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_id = 'user-create-form'
            self.helper.form_method = 'POST'
            self.helper.form_action = 'register'
            self.helper.help_text_inline = True
            self.helper.form_show_labels = False
            self.helper.add_input(Submit('submit', 'Submit'))
            self.helper.layout = Layout(
                Fieldset('Username',
                    HTML('<p>Your username will be:</p>'),
                    HTML('<p id="LOL"><strong></strong></p>'),
                    Field('first_name', placeholder='First Name',),
                    Field('last_name', placeholder='Last Name'),),
                Fieldset('Password',
                    Alert("Passwords <strong>must</strong> be at least 8 characters long."),
                    Field('password1', placeholder='Password'),
                    Field('password2', placeholder='Re-enter password'))
            )


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['email']