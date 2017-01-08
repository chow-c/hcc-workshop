from django import forms
from django.contrib.auth.models import User

from home.models import NewsletterSignup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, HTML
from crispy_forms.bootstrap import Field, Alert, PrependedText

class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"].replace(" ", "") # Remove all white space
        user.last_name = self.cleaned_data["last_name"].replace(" ", "") # Remove all white space

        temp_username = user.first_name.lower() + "." +user.last_name.lower()

        if User.objects.filter(username__iexact=temp_username).exists():
            temp_username = temp_username + \
                            str(User.objects.filter(username__startswith=temp_username).count()+1)
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
            Fieldset('<span style="text-align: left"> \
            Username</span><span style="font-size: 0.4em; position: relative; left: 35%;"> \
            Already have an account? <a href="{% url "login" %}" style="text-decoration: underline;" > \
            Login here.</a></span>',
                     PrependedText('first_name',
                                   '<i class="fa fa-user" aria-hidden="true"></i>',
                                   placeholder='First Name',),
                     PrependedText('last_name',
                                   '<i class="fa fa-user-o" aria-hidden="true"></i>',
                                   placeholder='Last Name'),
                     HTML('<p class="col-lg-6"> \
                           <i class="fa fa-id-card-o" aria-hidden="true"></i>&nbsp;&nbsp; \
                           Your username will be: </p><p id="LOL" class="col-lg-6"></p>'),
                    ),
            Fieldset('Password',
                     Alert("Passwords <strong>must</strong> be at least 8 characters long."),
                     PrependedText('password1',
                                   '<i class="fa fa-lock" aria-hidden="true"></i>',
                                   placeholder='Password'),
                     PrependedText('password2',
                                   '<i class="fa fa-lock" aria-hidden="true"></i>',
                                   placeholder='Re-enter password')),
            Field('')
            )


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        exclude = []

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'newsletter-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'newsletter'
        self.helper.form_show_labels = False
        self.helper.error_text_inline = False
        self.helper.html5_required = False
        self.helper.add_input(Submit('submit', 'Subscribe'))
        self.helper.layout = Layout(
            HTML('<p class="text-center">Great! We need just a bit more information.</p>'),
            PrependedText('first_name',
                          '<i class="fa fa-user" aria-hidden="true"></i>',
                          placeholder='First Name'),
            PrependedText('last_name',
                          '<i class="fa fa-user" aria-hidden="true"></i>',
                          placeholder='Last Name'),
            PrependedText('email',
                          '<i class="fa fa-envelope" aria-hidden="true"></i>',
                          placeholder='Email'),
            PrependedText('school',
                          '<i class="fa fa-building" aria-hidden="true"></i>',
                          placeholder='School'),
            PrependedText('year',
                          '<i class="fa fa-graduation-cap" aria-hidden="true"></i>',
                          placeholder='Year of study'),
            PrependedText('area_of_interest',
                          '<i class="fa fa-star" aria-hidden="true"></i>',
                          placeholder='Area of interest (eg: Engineering or Computer Science)'),
        )

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'user-login-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = 'login'
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.layout = Layout(
            PrependedText('username',
                          '<i class="fa fa-user" aria-hidden="true"></i>',
                          placeholder="firstname.lastname"),
            PrependedText('password',
                          '<i class="fa fa-lock" aria-hidden="true"></i>',
                          placeholder="Password"),
        )
