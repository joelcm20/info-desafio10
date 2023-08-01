from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from apps.recetas.models import Receta
from .models import Comentario
from django.contrib.auth.decorators import user_passes_test
from apps.usuario.utils import is_registered, is_collaborator

# Create your views here.

@user_passes_test(is_registered) # este decorador verifica que el usuario sea un usuario registrado
def crearComentario(request): # funcionalidad para que un usuario pueda crear un nuevo comentario hacia una receta en especifico segun su id
    if request.method == "POST":
        receta_id = request.POST["receta"]
        texto = request.POST["texto"]
        receta = get_object_or_404(Receta, id=receta_id)
        usuario = request.user
        Comentario.objects.create(receta=receta, usuario=usuario, texto=texto)
        return redirect("detalle-receta", id=receta_id)

@user_passes_test(is_registered) # este decorador verifica que el usuario sea un usuario registrado
def borrarComentario(request, id):# funcion para borrar un comentario en especifico segun su id, los colaboradores podran borrar todos, pero un usuario normal solo los propios
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
