
from django.urls import path
from .views import todo_list_create,todo_home



urlpatterns = [
    path("",todo_home),
    path("list-create/", todo_list_create)
]
