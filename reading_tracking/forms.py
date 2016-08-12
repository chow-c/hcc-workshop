from django import forms

from reading_tracking.models import ReadingEyegaze

class ReadingEyegazeForm(forms.ModelForm):
    class Meta:
        model = ReadingEyegaze
        fields = ['gazedata']
