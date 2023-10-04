from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index_view'))
    else:  
        form = UserLoginForm()
    context = {
        'title': 'Login',
        'form': form 
    }
    return render(request, 'users/login.html', context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login_view'))
        
    form = UserRegisterForm()
    context = {
        'title': 'Registratsiya',
        "form" : form
    }
    return render(request, 'users/register.html', context)


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index_view'))