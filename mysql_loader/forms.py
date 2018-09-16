from django import forms
from .models import Names



class AddNameForm(forms.ModelForm):
    
    class Meta:
        model = Names
        fields = ['name']
