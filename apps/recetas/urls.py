from django.urls import path
from apps.recetas import views

urlpatterns = [
    path("", views.getReceta, name="receta"),
    path("detalle/<int:id>", views.detalleReceta, name="detalle-receta"),
    path("crear/", views.crearReceta, name="crear-receta"),
    path("borrar/<int:id>", views.borrarReceta, name="borrar-receta"),
    path("actualizar-receta/<int:id>", views.actualizarReceta, name="actualizar-receta")
]