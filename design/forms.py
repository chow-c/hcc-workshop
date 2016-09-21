from .models import Mappings, Constraints
from django import forms
from django.utils.translation import ugettext_lazy as _

class mappingsForm(forms.ModelForm):
    class Meta:
        model = Mappings
        fields = ['answer']
        labels = {
            'answer': _('What makes a good mapping?'),
        }
        widgets = {
            'answer': forms.RadioSelect(),
        }

class constraintForm(forms.ModelForm):
    class Meta:
        model = Constraints
        fields = ['answer']
        labels = {
            'answer': _('Why are constraints used?'),
        }
        widgets = {
            'answer': forms.RadioSelect(),
        }