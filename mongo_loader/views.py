from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404  
from django.utils import timezone


## BASIC VIEWS

def mongo_loader(request):
    
    return render(request, "mongo_loader.html")