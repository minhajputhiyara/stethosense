from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserAdminCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *
from django import forms
from django. contrib import messages



def home(request):
    return render(request, 'base.html')

@csrf_exempt
def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('base.html')
        else:
            messages.info(request, 'Password or Username is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')



def signup(request):

    form = UserAdminCreationForm()
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('first_name')

            messages.success(request, 'Account Created for ' + str(user) + ' Please login')
            return redirect('login')
    return render(request, 'signup.html', {'form': form})