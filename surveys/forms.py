from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from surveys.models import Response

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, HTML
from crispy_forms.bootstrap import Field, Alert, PrependedText

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response']

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'response-form'
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Submit'))
