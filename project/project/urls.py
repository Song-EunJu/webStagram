from django.contrib import admin
from django.urls import path, include
from account.views import register_view
from webstagram.views import feed 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_view, name="first"),
    path('feed/', feed, name="feed"),
    path('account/', include('account.urls')),
    path('webstagram/', include('webstagram.urls')),
]
