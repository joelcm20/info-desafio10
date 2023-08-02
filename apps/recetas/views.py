from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import JsonResponse, HttpResponse
import json
from .forms import RecetaForm, CategoriaForm
from .models import Receta, Categoria
from apps.comment.models import Comentario
from apps.comment.forms import CommentForm
from django.contrib.auth.decorators import user_passes_test
from apps.usuario.utils import is_registered, is_collaborator


# Create your views here.

# funcion para obtener todas las recetas, funcionalidad/logica de filtros
# y funcionalidad para borrar una receta
def getReceta(request):
    recetas = Receta.objects.all()

    if request.method == "POST" and "buscar-recetas" in request.POST:
        nombre_recetas = request.POST.get("buscar-recetas")
        recetas = recetas.filter(nombre__icontains=nombre_recetas)

    categoria = request.GET.get('categoria')
    if categoria:
        recetas = recetas.filter(id_categoria=categoria)

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

# funcion para objeter una receta especifica por su id con toda su informacion
# incluyendo comentarios


def detalleReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    comments = Comentario.objects.filter(receta=receta)
    return render(request, "detalle-receta.html", {
        "receta": receta,
        "comments": comments,
        "form": CommentForm})


# este decorador verifica que el usuario sea un colaborador
@user_passes_test(is_collaborator)
# funcion para renderizar template para crear receta y logica para crear receta
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


# este decorador verifica que el usuario sea un colaborador
@user_passes_test(is_collaborator)
def borrarReceta(request, id):  # funcion para borrar una receta en especifico segun el id
    if request.method == "POST":
        usuario = request.user
        receta = get_object_or_404(Receta, id=id, usuario=usuario)
        Receta.delete(receta)
        return redirect("receta")


# este decorador verifica que el usuario sea un colaborador
@user_passes_test(is_collaborator)
# funcion para actualizar los datos de una receta existente y tambien renderiza el formulario para hacerlo
def actualizarReceta(request, id):
    receta = get_object_or_404(Receta, id=id)
    form = RecetaForm(instance=receta)

    if request.method == "GET":
        return render(request, "actualizar-receta.html", {"form": form})

    form = RecetaForm(request.POST, request.FILES, instance=receta)
    form.save()
    return redirect("detalle-receta", id)


# este decorador verifica que el usuario sea un colaborador
@user_passes_test(is_collaborator)
# funcion para obtener todas las categorias y logica para eliminar una en especifico segun su id
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


@user_passes_test(is_collaborator)
def editarCategoria(request, id):
    if request.method != "POST":
        return JsonResponse({'msg': 'metodo no permitido!'}, status=405)

    usuario = request.user
    categoria = get_object_or_404(Categoria, id=id)

    data = json.load(request)
    nueva_categoria = data.get("nombre")
    categoria.nombre = nueva_categoria
    categoria.save()
    return JsonResponse({'msg': 'Categoria actualizado correctamente.'})
