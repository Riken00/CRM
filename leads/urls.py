from django.urls import path
from .views import home_page , table_data,table_create
urlpatterns = [
    path('',home_page),
    path('<int:pk>/',table_data),        # here <pk> will be take as a primary key from the domain and send the value from the view func.
    path('create/',table_create),        # here <pk> will be take as a primary key from the domain and send the value from the view func.

]
