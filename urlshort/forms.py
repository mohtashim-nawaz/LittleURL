from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model = ShortURL