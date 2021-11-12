from django import forms
from django.http.response import HttpResponse
from django.shortcuts import render

from leads.forms import form_table
from .models  import Leads,Agents,User
from .forms import form_table 
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



def table_data(request,pk):  # here pk will be take the value from the domain like if there is value like 5 than the pk will be 5   <pk> django will take it automaticaly detact it as that we wants to use as the primary key and every pk will be primary key
    # print(pk)                        # i.e  http://127.0.0.1:8000/lead/54   pk will be 54
    sss = User.objects.get(id=pk)
    contex = {
        "Lead" : sss

    }   
    print(sss,'-----------------')                        # i.e  http://127.0.0.1:8000/lead/54   pk will be 54
    return render(request,'secound.html',contex)
    # return HttpResponse(f'This is the table {pk}')
    

def table_create(request):
    print(request.POST)
    req = request.POST
    form = form_table()
    if request.method == "POST" :
        print('i got the request')
        form = form_table(request.POST)
        if form.is_valid():
            print('this is the valid form')
            first_name = form.cleaned_data['first_name']
            last_nmae = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agents.objects.first()
            Leads.objects.create(first_name=first_name,last_name=last_nmae,age=age,agent=agent)
            print('All Done----------- !')

    contex = {
        "Lead" : form,
        "req" : req
    }
    return render(request,'forms.html',contex)
