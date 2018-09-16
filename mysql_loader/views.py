from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone
from .models import Names
from .forms import AddNameForm

## BASIC VIEWS

def mysql_loader(request):
    
    names = Names.objects.all()
    
    return render(request, "mysql_loader.html", {'names': names } )
    
    
def add_name(request):
    
    form = AddNameForm(request.POST)
    
    if request.method == 'POST':
        
        form = AddNameForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            
            
            new_name = Names.objects.create(name = name)
            
            new_name.save()
            
            return redirect(reverse('mysql_loader'))
            
    return render(request, "add_name.html", {'form': form })        
    
    
