from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from leads.forms import form_table
from .models  import Leads,Agents,User
from .forms import  from_table_model
# Create your views here.

def home_page(request):
    Lead=Leads.objects.all()
    print(Lead)
    a = {
        "name" : "Riken",
        "Lead" : Lead,
        "Aatak" : "Khaddela"
    }
    return render(request,'leads/home.html',a)        
    # return render(request,'secound.html')



def table_data(request,pk):  # here pk will be take the value from the domain like if there is value like 5 than the pk will be 5   <pk> django will take it automaticaly detact it as that we wants to use as the primary key and every pk will be primary key
    # print(pk)                        # i.e  http://127.0.0.1:8000/lead/54   pk will be 54
    sss = Leads.objects.get(id=pk)
    contex = {
        "Lead" : sss,
        "pk" : pk
    }   
    print(sss,'-----------------')                        # i.e  http://127.0.0.1:8000/lead/54   pk will be 54
    return render(request,'leads/secound.html',contex)
    # return HttpResponse(f'This is the table {pk}')
    


def table_create(request):
    print(request.POST)
    req = request.POST
    form = from_table_model()
    if request.method == "POST" :
        print('i got the request')
        form = from_table_model(request.POST)
        if form.is_valid():
            print('this is the valid form')
            form.save()
            print('All Done----------- !')
            return redirect("/lead")

    contex = {
        "Lead" : form,
        "req" : req
    }
    return render(request,'leads/forms.html',contex)
# def table_create(request):
    # print(request.POST)
    # req = request.POST
    # form = from_table_model()
    # if request.method == "POST" :
    #     print('i got the request')
    #     form = from_table_model(request.POST)
    #     if form.is_valid():
    #         print('this is the valid form')
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = Agents.objects.first()

    #         Leads.objects.create(first_name=first_name,last_name=last_name,age=age,agent=agent)
    #         print('All Done----------- !')
    #         return redirect("/lead")

    # contex = {
    #     "Lead" : form,
    #     "req" : req
    # }
    # return render(request,'forms.html',contex)


def table_update(request,pk):
    print(request.POST)
    req = request.POST
    Lead = Leads.objects.get(id=pk)
    form = from_table_model()
    if request.method == "POST" :
        form = from_table_model(request.POST,instance=Lead)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # Lead.first_name = first_name
            # Lead.last_name = last_name
            # Lead.age = age                         Not require we can do it by django inbuilt functions through add (instace = Lead) in form line : 80      and write direct form.save()   but we can use it when we wants to use it to update any data 

            form.save()
        print('All Done----------- !')
        return redirect("/lead")

    contex = {
        "Lead" : form,
        "req" : req
    }
    # return render(request,'forms.html',contex)


    return render(request,'leads/updateforms.html',contex)

def delete_forms(request,pk):
    Lead = Leads.objects.get(id=pk)
    Lead.delete()
    return redirect("/lead/")

print('Completed')