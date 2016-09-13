from django import forms
from .models import Questionnaire, ExperimentPage
from django.utils.translation import ugettext_lazy as _

class questionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['age','gender','education', 'major', 'language','vision']
        labels = {
            'education': _('What level of education have you completed (or currently completing)?'),
            'major': _('What is/was your major/field of study?' ),
            'language': _('What is your native language?' ),
            'vision': _('Do you have normal, or corrected to normal, vision? (Note: if you wear glasses or contacts answer yes)' ),
        }

class experimentForm(forms.ModelForm):
    class Meta:
        model = ExperimentPage
        fields = ['answer', 'gazedata','question_number', 'image_ref']