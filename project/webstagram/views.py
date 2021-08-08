from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from account.models import CustomUser


def feed(request):
    return render(request, "feed.html")

def profile(request, writerId):
    user=get_object_or_404(CustomUser, username = writerId)
    return render(request, "profile.html", {'user':user})

def edit(request, writerId): # 프로필 수정 
    edit_user = CustomUser.objects.get(username = writerId)
    return render(request, 'edit.html', {'edit':edit_user})

def update(request, writerId): # 프로필 업데이트
    update_user = CustomUser.objects.get(username = writerId)
    update_user.nickname = request.POST['nickname']
    update_user.profileMsg = request.POST['message']
    update_user.profileImg = request.FILES.get('image', None)
    update_user.save()  
    return redirect('profile', update_user.username)
