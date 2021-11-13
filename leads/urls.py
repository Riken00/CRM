from django.urls import path
from .views import home_page , table_data,table_create,table_update,delete_forms

app_name = 'leads'
urlpatterns = [
    path('',home_page,name='home-forms'),
    path('<int:pk>/',table_data,name='primary-key'),        # here <pk> will be take as a primary key from the domain and send the value from the view func.
    path('create/',table_create,name='create-forms'),        # here <pk> will be take as a primary key from the domain and send the value from the view func.
    path('<int:pk>/update/',table_update,name='update-forms'),
    path('<int:pk>/delete/',delete_forms,name='delete-forms'),
]

    