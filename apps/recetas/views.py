from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import RecetaForm
from .models import Receta
from apps.comment.models import Comentario
from apps.comment.forms import CommentForm
from django.contrib.auth.decorators import user_passes_test
from apps.usuario.utils import is_registered


# Create your views here.

#ejemplo
@user_passes_test(is_registered)
def getReceta(request):
    if request.method == "POST" and "borrar-recetas" in request.POST:
        usuario = request.user
        receta_id = int(request.POST["borrar-recetas"])
        receta = get_object_or_404(Receta, id=receta_id, usuario=usuario)
        Receta.delete(receta)

    receta = Receta.objects.all()
    return render(request, "receta.html", {"receta": receta})


def detalleReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    comments = Comentario.objects.filter(receta=receta)
    return render(request, "detail-news.html", {
        "receta": receta,
        "comments": comments,
        "form": CommentForm})


def crearReceta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("receta")
        else:
            return render(request, "crear-receta.html", {
                "form": RecetaForm,
                "error": "Form is not valid!"
            })
    else:
        form = RecetaForm()
        return render(request, "crear-receta.html", {
            "form": form
        })


def borrarReceta(request, id):
    if request.method == "POST":
        usuario = request.user
        receta = get_object_or_404(Receta, id=id, usuario=usuario)
        Receta.delete(receta)
        return redirect("receta")


def actualizarReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    form = RecetaForm(instance=receta)

    if request.method == "GET":
        return render(request, "actualizar-receta.html", {"form": form})

    form = RecetaForm(request.POST, request.FILES, instance=receta)
    form.save()
    return redirect("detalle-receta", id)
