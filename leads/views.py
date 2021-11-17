from typing import List
from django.urls import reverse
from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import from_table_model
from .models  import Leads,Agents,User
from .forms import  from_table_model
from django.views import generic # or 
from django.views.generic import TemplateView,ListView, UpdateView, DetailView,DeleteView,CreateView


# Create your views here..



# CRUD+L - Create, Retrieve , update, and delete  + List

class LandingPageview(generic.TemplateView):
    template_name="home.html"
          
def landing_page(request):
    return render(request,'home.html')

# -------------------------------------------------------------------------------------------------------------------

class Leadlistview(ListView):
    Template_name = "leads/leads_list.html.html"
    context_object_name = "Lead"
    queryset = Leads.objects.all()


def home_page(request):
    Lead=Leads.objects.all()
    print(Lead)
    a = {
        "name" : "Riken",
        "Lead" : Lead,
        "Aatak" : "Khaddela"
    }
    return render(request,'leads/lead_list.html.html',a)        
    # return render(request,'secound.html')

# -------------------------------------------------------------------------------------------------------------------


class Leadlistdetail(DetailView):
    template_name = "leads/detail_lead.html"
    queryset = Leads.objects.all()
    context_object_name = "Lead"   # if we don't wanna use this line then we have to specify the "object_list" instad of the Lead this is by defualt || otherwise we can set another name like "Lead" by useing this line of code



def table_data(request,pk):  # here pk will be take the value from the domain like if there is value like 5 than the pk will be 5   <int:pk> django will take it automaticaly detact it as that we wants to use as the primary key and every pk will be primary key
    # print(pk)                        # i.e  http://127.0.0.1:8000/lead/54   pk will be 54
    sss = Leads.objects.get(id=pk)
    contex = {
        "Lead" : sss,
        "pk" : pk
    }   
    print(sss,'-----------------')                        # i.e  http://127.0.0.1:8000/lead/54   pk will be 54
    return render(request,'leads/detail_lead.html',contex)
    # return HttpResponse(f'This is the table {pk}')
    
# -------------------------------------------------------------------------------------------------------------------


class Leadcreateview(CreateView):
    template_name = "leads/createlead.html"
    form_class = from_table_model

    def get_success_url(self) :
        return reverse("leads:home-forms")





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
            return redirect("leads:home-forms")

    contex = {
        "Lead" : form,
        "req" : req
    }
    return render(request,'leads/createlead.html',contex)
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

# -------------------------------------------------------------------------------------------------------------------

class Leadupdateview(UpdateView):
    template_name = "leads/updateforms.html"
    form_class = from_table_model
    # context_object_name = "Lead"

    # def get_success_url(self) :
    #     return reverse("leads:update-forms")
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Leads.objects.all()

    def get_success_url(self):
        return reverse("leads:home-forms")

# def table_update(request,pk):
#     print(request.POST)
#     req = request.POST
#     Lead = Leads.objects.get(id=pk)
#     form = from_table_model()
#     if request.method == "POST" :
#         form = from_table_model(request.POST,instance=Lead)
#         if form.is_valid():
#             # first_name = form.cleaned_data['first_name']
#             # last_name = form.cleaned_data['last_name']
#             # age = form.cleaned_data['age']
#             # Lead.first_name = first_name
#             # Lead.last_name = last_name
#             # Lead.age = age                         Not require we can do it by django inbuilt functions through add (instace = Lead) in form line : 80      and write direct form.save()   but we can use it when we wants to use it to update any data 

#             form.save()
#         print('All Done----------- !')
#         return redirect("/lead")

#     contex = {
#         "Lead" : form,
#         "req" : req
#     }
#     # return render(request,'forms.html',contex)

    

#     return render(request,'leads/updateforms.html',contex)

# -------------------------------------------------------------------------------------------------------------------
class Leaddeleteview(DeleteView):
    template_name = "leads/delete_list.html"
    queryset = Leads.objects.all()

    def get_success_url(self):
        return reverse("leads/leads_list.html")

def delete_forms(request,pk):
    Lead = Leads.objects.get(id=pk)
    Lead.delete()
    return redirect("/lead/")

print('Completed')

# ---------------------------------------------------------------------------------------------------------------------------