from django import forms

from join_the_dots.models import DotsEyegaze

class DotsEyegazeForm(forms.ModelForm):
    class Meta:
        model = DotsEyegaze
        fields = ['gazedata']