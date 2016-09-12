from django import forms

from eyetracking.models import DotsGaze, ReadingGaze

# For the join the dots app
class DotsGazeForm(forms.ModelForm):
    class Meta:
        model = DotsGaze
        fields = ['gazedata']

# For the reading tracking app
class ReadingGazeForm(forms.ModelForm):
    class Meta:
        model = ReadingGaze
        fields = ['gazedata']