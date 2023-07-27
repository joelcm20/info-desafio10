from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from apps.recetas.models import Receta
from .models import Comentario
from apps.usuario.utils import is_collaborator

# Create your views here.


def crearComentario(request):
    if request.method == "POST":
        receta_id = request.POST["receta"]
        texto = request.POST["texto"]
        receta = get_object_or_404(Receta, id=receta_id)
        usuario = request.user
        Comentario.objects.create(receta=receta, usuario=usuario, texto=texto)
        return redirect("detalle-receta", id=receta_id)


def borrarComentario(request, id):
    if not request.method == "POST":
        return HttpResponse(status=404)

    comentario = get_object_or_404(Comentario, id=id)
    usuario = request.user

    if is_collaborator(usuario):
        Comentario.delete(comentario)
        return redirect("detalle-receta", comentario.receta.id)

    if not comentario.usuario == usuario:
        return redirect("detalle-receta", comentario.receta.id)

    Comentario.delete(comentario)
    return redirect("detalle-receta", comentario.receta.id)
