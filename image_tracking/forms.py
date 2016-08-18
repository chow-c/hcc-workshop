from django import forms

from image_tracking.models import ImageEyegaze

class ImageEyegazeForm(forms.ModelForm):
    class Meta:
        model = ImageEyegaze
        fields = ['image1','image2','image3']