from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.crearComentario, name="create-comment"),
    path("delete/<int:id>", views.borrarComentario, name="delete-comment"),
    path("edit/<int:id>", views.editarComentario, name="editar-comentario")
]
