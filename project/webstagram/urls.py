from django.urls import path
from .views import *

urlpatterns = [
    path('feed/', feed, name="feed"),
    path('profile/<str:writerId>', profile, name="profile"),
]