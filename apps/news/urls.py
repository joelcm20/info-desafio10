from django.urls import path
from apps.news import views

urlpatterns = [
    path("", views.getNews, name="news"),
    path("detail/<int:id>", views.detailNews, name="detail-news"),
    path("create/", views.createNews, name="create-news"),
    path("delete/<int:id>", views.deleteNews, name="delete-news"),
    path("update-news/<int:id>", views.updateNews, name="update-news")
]