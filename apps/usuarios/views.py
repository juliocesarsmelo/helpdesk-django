from django.shortcuts import render, redirect
from django.contrib.auth import logout as logout_django
from django.http import HttpResponse

def login(request):
    if request.method == "GET":
        return render(request, "usuarios/login.html")
    
def logout(request):
    logout_django(request)
    return redirect("login")

def sign_up(request):
    if request.method == "GET":
        return render(request, "usuarios/sign_up.html")