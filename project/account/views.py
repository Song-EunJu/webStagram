from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        user = authenticate(request=request, username=id, password=password)
        if user is not None:  # 유저가 있는 경우
            login(request, user)   
            return render(request, 'feed.html', {'user':user})
        # else: # 유저가 없는경우
        #     return 
        #     messages.info(request, '사용자의 정보가 없습니다')
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    if request.method == 'POST':
        new_user = CustomUser()
        new_user.nickname = request.POST['nickname']
        new_user.username = request.POST['id']
        if request.POST['password1'] == request.POST['password2']:
            new_user.set_password(request.POST['password1'])
            new_user.save()
            login(request, new_user)
            return render(request,'feed.html', {'new_user':new_user})
        # else:
        #     return messages.info(request, '비밀번호가 일치하지 않습니다.')
    else:
        return render(request, "signup.html")
