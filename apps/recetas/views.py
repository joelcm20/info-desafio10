from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import RecetaForm, CategoriaForm
from .models import Receta, Categoria
from apps.comment.models import Comentario
from apps.comment.forms import CommentForm
from django.contrib.auth.decorators import user_passes_test
from apps.usuario.utils import is_registered, is_collaborator


# Create your views here.
def getReceta(request):
    recetas = Receta.objects.all()


    categoria = request.GET.get('id_categoria')
    if categoria:
        recetas = recetas.filter(categoria=categoria)

  
    if 'antiguedad_asc' in request.GET:
        recetas = recetas.order_by('fecha_publicacion')
    elif 'antiguedad_desc' in request.GET:
        recetas = recetas.order_by('-fecha_publicacion')
    elif 'orden_asc' in request.GET:
        recetas = recetas.order_by('nombre')
    elif 'orden_desc' in request.GET:
        recetas = recetas.order_by('-nombre')


    if request.method == "POST" and "borrar-recetas" in request.POST:
        usuario = request.user
        receta_id = int(request.POST["borrar-recetas"])
        receta = get_object_or_404(Receta, id=receta_id, usuario=usuario)
        Receta.delete(receta)


    categorias = Categoria.objects.all()  # Asume que tienes un modelo Categoria

    return render(request, "recetas.html", {"recetas": recetas, "categorias": categorias})


def detalleReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    comments = Comentario.objects.filter(receta=receta)
    return render(request, "detalle-receta.html", {
        "receta": receta,
        "comments": comments,
        "form": CommentForm})


@user_passes_test(is_collaborator)
def crearReceta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.usuario = request.user
            form.save()
            return redirect("recetas")
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

@user_passes_test(is_collaborator)
def borrarReceta(request, id):
    if request.method == "POST":
        usuario = request.user
        receta = get_object_or_404(Receta, id=id, usuario=usuario)
        Receta.delete(receta)
        return redirect("receta")

@user_passes_test(is_collaborator)
def actualizarReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    form = RecetaForm(instance=receta)

    if request.method == "GET":
        return render(request, "actualizar-receta.html", {"form": form})

    form = RecetaForm(request.POST, request.FILES, instance=receta)
    form.save()
    return redirect("detalle-receta", id)

@user_passes_test(is_collaborator)
def getCategorias(request):
    if request.method == "POST" and not "eliminar-categoria" in request.POST:
        nombre_categoria = request.POST["nombre"]
        Categoria.objects.create(nombre=nombre_categoria)
        return redirect("categorias")

    if request.method == "POST" and "eliminar-categoria" in request.POST:
        categoria_id = request.POST["eliminar-categoria"]
        categoria = get_object_or_404(Categoria, id=categoria_id)
        Categoria.delete(categoria)
        return redirect("categorias")

    categorias = Categoria.objects.all()
    return render(request, "categorias.html", {
        "categorias": categorias,
        "form": CategoriaForm
    })
