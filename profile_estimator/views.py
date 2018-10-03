from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone
from .forms import SkillsForm
from .models import DataSkill
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
    dataskills = DataSkill.objects.values()
    # dataskills = dataskills.objects.values()
    check = [type(dataskills)]
    
    # results = []
    # for element in skills:
    #     res = 0
    #     if element in dataskills:
    #         res += dataskills[element]
    #     results.append(res)
        
    results = 0
    for element in skills:
        results += dataskills.get(element, 0)
        
    
    
    return render(request, "estimate.html",  {'skills': skills, 'dataskills': dataskills, 'check': check, 'results': results })