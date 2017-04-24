from django import forms
from .models import Kontrakt

class PostForm(forms.ModelForm):

    class Meta:
        model=Kontrakt
        fields=('RCP',)