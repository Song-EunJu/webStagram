from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from account.models import CustomUser
# from .models import Blog
# from .forms import BlogForm

def feed(request):
    return render(request, "feed.html")

def profile(request, writerId):
    writer=get_object_or_404(CustomUser, username = writerId)
    return render(request, "profile.html", {'writer':writer})