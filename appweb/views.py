from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def principal(request):
    return render(request, "principal.html")

def informacion(request):
    return render(request, "informacion.html")
