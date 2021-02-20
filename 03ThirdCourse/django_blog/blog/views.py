from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from blog.models import ArticleModel
from django.utils import timezone
# from blog.forms import ArticleForm


class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog!")

    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog!")


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, "articles.html", {"articles": articles})

    def post(self, request):
        title = request.POST["title"]
        category = request.POST["category"]
        author = request.POST["author"]
        content = request.POST["content"]

        ArticleModel.objects.create(title=title, category=category, author=author, content=content,
                                    creation_date=datetime.now(tz=timezone.utc))

        return redirect("/blog/articles")