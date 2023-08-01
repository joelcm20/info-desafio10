from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from apps.usuario.models import Usuario
from django.db import IntegrityError

# funcion que renderiza el el template home
def home(request):
    return render(request, "home.html")

# funcion para registrar usuarios y renderizar el template signup
def signUp(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})

    if not request.POST["password1"] == request.POST["password2"]:
        return render(request, "signup.html", {"form": UserCreationForm, "error": "passwords do not match"})

    try:
        usuario = Usuario.objects.create_user(
            username=request.POST["username"], password=request.POST["password1"])
        usuario.save()
        login(request, usuario)
        return redirect("recetas")
    except IntegrityError:
        return render(request, "signup.html", {"form": UserCreationForm, "error": "user already exists. please try a different username."})

# funcion para desloguearse o cerrar session
def signOut(request):
    logout(request)
    return redirect("home")

# funcion para iniciar session
def signIn(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})

    username = request.POST["username"]
    password = request.POST["password"]
    usuario = authenticate(request, username=username, password=password)

    if usuario is None:
        return render(request, "signin.html", {"form": AuthenticationForm, "error": "username and password do not match"})
    login(request, usuario)
    return redirect("recetas")

# funcion para renderizar el template acercade
def acercaDe(request):
    return render(request, "acercade.html")