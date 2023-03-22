from django import forms
from django.forms import ModelForm
from .models import Picture

class ImageForm(ModelForm):
    class Meta:
        model = Picture
        fields = {'image'}
