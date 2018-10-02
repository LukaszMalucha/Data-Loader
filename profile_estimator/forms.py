from django import forms
from django.forms import ModelForm, Textarea
from .models import Skills




class SkillsForm(forms.ModelForm):
    
    class Meta:
        model = Skills
        fields = ['skills']
        widgets = {
            'skills': forms.Textarea(),
        }