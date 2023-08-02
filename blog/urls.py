"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from apps.recetas.views import getCategorias, editarCategoria

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.home, name="home"),
    path("categorias", getCategorias, name="categorias"),
    path("editar-categoria/<int:id>", editarCategoria, name="categorias-editar"),
    path("sign-up/", views.signUp, name="sign-up"),
    path("sign-out", views.signOut, name="sign-out"),
    path("sign-in", views.signIn, name="sign-in"),
    path("acerca-de", views.acercaDe, name="acerca-de"),
    path("recetas/", include("apps.recetas.urls")),
    path("comment/", include("apps.comment.urls")),
    path('', include('apps.contacto.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
