from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
# from django.contrib.auth.forms import UserCreationForm
from . import models

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # user.profile.dob = form.cleaned_data.get('dob')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password= raw_password)
            login(request,user)
            return redirect('account:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html',{'form':form})

def index(request):
    return render(request, 'account/index.html')


