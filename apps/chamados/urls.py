from django.urls import path
from . import views

app_name = "chamados"

urlpatterns = [
    path("", views.index, name="index")
]
