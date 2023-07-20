from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from apps.news.models import News
from .models import Comment

# Create your views here.


def createComment(request):
    if request.method == "POST":
        news_id = request.POST["news"]
        comment = request.POST["text"]
        news = get_object_or_404(News, id=news_id)
        user = request.user
        Comment.objects.create(news=news, user=user, text=comment)
        return redirect("detail-news", id=news_id)

def deleteComment(request, id):
    if not request.method == "POST":
        return HttpResponse(status=404)
    
    comment = get_object_or_404(Comment, id=id)
    user = request.user
    if not comment.user == user:
        return redirect("detail-news", comment.news.id)
    
    Comment.delete(comment)
    return redirect("detail-news", comment.news.id)

    

