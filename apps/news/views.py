from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import NewsForm
from .models import News
from apps.comment.models import Comment
from apps.comment.forms import CommentForm

# Create your views here.


def getNews(request):
    if request.method == "POST" and "delete-news" in request.POST:
        user = request.user
        news_id = int(request.POST["delete-news"])
        news = get_object_or_404(News, id=news_id, user=user)
        News.delete(news)

    news = News.objects.all()
    return render(request, "news.html", {"news": news})


def detailNews(request, id):
    news = get_object_or_404(News, id=id)
    comments = Comment.objects.filter(news=news)
    return render(request, "detail-news.html", {
        "news": news,
        "comments": comments,
        "form": CommentForm})


def createNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("news")
        else:
            return render(request, "create-news.html", {
                "form": NewsForm,
                "error": "Form is not valid!"
            })
    else:
        form = NewsForm()
        return render(request, "create-news.html", {
            "form": form
        })


def deleteNews(request, id):
    if request.method == "POST":
        user = request.user
        news = get_object_or_404(News, id=id, user=user)
        News.delete(news)
        return redirect("news")


def updateNews(request, id):
    news = get_object_or_404(News, id=id)
    form = NewsForm(instance=news)

    if request.method == "GET":
        return render(request, "update-news.html", {"form": form})
    
    form = NewsForm(request.POST, request.FILES, instance=news)
    form.save()
    return redirect("detail-news", id)
