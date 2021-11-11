from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Leads,Agents,User

# Create your views here.

def home_page(request):
    Lead=User.objects.all()
    a = {
        "name" : "Riken",
        "Lead" : Lead,
        "Aatak" : "Khaddela"
    }
    return render(request,'home.html',a)
    # return render(request,'secound.html')


    