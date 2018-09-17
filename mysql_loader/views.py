from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone
from .models import Names, Document
from .forms import AddNameForm, DocumentForm
import os
import csv

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
    
    
def delete_names(request):
    

    names = Names.objects.all()
    names.delete()
        
    return redirect(reverse('mysql_loader'))
    
    
def add_document(request):
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            
            
            
            return redirect('mysql_loader')
    else:
        form = DocumentForm()
    return render(request, 'add_document.html', {'form': form })    
    
def manage_documents(request):
    
    mypath = 'media/documents'
    files = os.listdir(mypath)
    
    
    return render(request, 'manage_documents.html', {'files': files})
    
    
def database_upload(request, file):
    
    names = []
    document = file 
    with open('media/documents/%s' % file) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Names.objects.get_or_create(name=row[0])
    
    
    
    
    return render(request, 'try.html', {'document': document, 'names': names})