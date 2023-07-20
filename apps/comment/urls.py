from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.createComment, name="create-comment"),
    path("delete/<int:id>", views.deleteComment, name="delete-comment")
]
