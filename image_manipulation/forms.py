from django import forms
from .models import ImagePage
from django.utils.translation import ugettext_lazy as _


class ImagePageForm(forms.ModelForm):
    class Meta:
        model = ImagePage
        fields = ['answer','image_number']
        labels = {
            'answer': _('Is this image manipulated?'),
        }
        widgets = {
            'answer': forms.RadioSelect(),
        }