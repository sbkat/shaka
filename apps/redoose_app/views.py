from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'redoose_app/index.html')

def search(request):
    return render(request, 'redoose_app/search.html')

def info(request):
    return render(request, 'redoose_app/info.html')

def purpose(request):
    return render(request, 'redoose_app/purpose.html')

def donate(request):
    return render(request, 'redoose_app/donate.html')

def subscribe(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='subscribe')
        return redirect('/subscription')
    else:
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        new_user.save()
        return redirect('/')

def subscription(request):
    return render(request, 'redoose_app/subscription.html')

