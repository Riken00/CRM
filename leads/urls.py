from django.urls import path
from .views import Leadcreateview,Leaddeleteview,Leadupdateview, Leadlistdetail, home_page , table_data,table_create,delete_forms ,Leadlistview,DetailView

app_name = 'leads'
urlpatterns = [
    path('',Leadlistview.as_view(),name='home-forms'),
    path('<int:pk>/',Leadlistdetail.as_view(),name='primary-key'),        # here <pk> will be take as a primary key from the domain and send the value from the view func.
    # path('create/',table_create,name='create-forms'),        # here <pk> will be take as a primary key from the domain and send the value from the view func.
    path('create/',Leadcreateview.as_view(),name='create-forms'),        # here <pk> will be take as a primary key from the domain and send the value from the view func.
    path('<int:pk>/update/',Leadupdateview.as_view(),name='update-forms'),
    path('<int:pk>/delete/',Leaddeleteview.as_view(),name='delete-forms'),
    # path('<int:pk>/delete/',delete_forms,name='delete-forms'),
]

    