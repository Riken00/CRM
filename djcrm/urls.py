from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lead/',include('leads.urls'),name='leads')
]
