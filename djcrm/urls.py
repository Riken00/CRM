from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from leads.views import landing_page , LandingPageview   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LandingPageview.as_view(),name='landing_page'),
    path('lead/',include('leads.urls'),name='leads')
]
