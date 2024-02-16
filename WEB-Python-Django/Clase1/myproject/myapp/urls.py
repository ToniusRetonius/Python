from os import name
from django.urls import path
from . import views

urlpatterns = [
    # cuando el usuario no escriba nada, lo mande al index 
    path("", views.index, name="index")
    path("empleados", views.empleados, name="empleados")
]