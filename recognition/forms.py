from django import forms

from recognition.models import UploadedImage


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image', 'fruit']
