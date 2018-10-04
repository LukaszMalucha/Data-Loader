from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone
from .forms import SkillsForm
from .models import DataSkill
import pandas as pd
import os
import csv



def profile(request):
    
    form = SkillsForm(request.POST)
    
    if request.method == 'POST':
        
        if form.is_valid():
            request.session['skills'] = request.POST['skills']
    
            return redirect(reverse('estimate'))
    
    return render(request, "profile.html",  {'form': form })
    
    
def estimate(request):
    
    skills = request.session.get('skills')
    skills = skills.split(',')
    
    
    
    dataskills = pd.DataFrame(list(DataSkill.objects.all().values()))
    check = [type(dataskills)]

        
    results = dataskills[dataskills['dataskill'].isin(skills)]
    results = results.iloc[:,[1,3]]
    results.set_index('dataskill', inplace=True)
    dictator = results.to_dict()
    dictator = dictator['percentage']
    
    
    return render(request, "estimate.html",  {'skills': skills, 'dataskills': dataskills.to_html(), 'check': check, 'results': results.to_html(), 'dictator': dictator })