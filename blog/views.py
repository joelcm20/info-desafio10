from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from apps.usuario.models import Usuario
from django.db import IntegrityError


def home(request):
    return render(request, "home.html")


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


def signOut(request):
    logout(request)
    return redirect("home")


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


def acercaDe(request):
    return render(request, "acercade.html")