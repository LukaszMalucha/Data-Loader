from django import forms
from .models import Names, Document



class AddNameForm(forms.ModelForm):
    
    class Meta:
        model = Names
        fields = ['name']



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )