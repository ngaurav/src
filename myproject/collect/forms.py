from django import forms
from .models import Collect

class CollectForm(forms.ModelForm):
    class Meta:
        model = Collect
        exclude = ()