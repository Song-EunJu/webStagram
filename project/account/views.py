from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id") 
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=id, password=password)
            if user is not None:
                login(request, user)   
        return redirect("home") 
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == 'POST':
        new_user = CustomUser()
        new_user.email=request.POST['email']
        new_user.name = request.POST['name']
        new_user.username = request.POST['id']
        new_user.set_password = request.POST['password']
        new_user.save()
        login(request, new_user)
        return render(request,'feed.html', {'new_user':new_user})
    else:
        return render(request, "signup.html")
