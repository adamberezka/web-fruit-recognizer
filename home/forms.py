from django import forms

from recognition.models import UploadedImage


class SearchForm(forms.Form):
    isPredictionRight = forms.BooleanField(required=False, label='Is Prediction Right')
    prediction = forms.CharField(max_length=32, required=False, widget=forms.Select(choices=UploadedImage.Fruit.choices))
    actual = forms.CharField(max_length=32, required=False, widget=forms.Select(choices=UploadedImage.Fruit.choices))
