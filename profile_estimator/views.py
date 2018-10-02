from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone
from .forms import SkillsForm
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
    
    
    return render(request, "estimate.html",  {'skills': skills })