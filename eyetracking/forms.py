from django import forms

from eyetracking.models import DotsGaze, ReadingGaze, ImageGaze

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

# For image tracking apply
class ImageGazeForm(forms.ModelForm):
    class Meta:
        model = ImageGaze
        fields = ['image1','image2','image3']