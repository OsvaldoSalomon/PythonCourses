from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from blog.models import ArticleModel

class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog!")

    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog!")


class Article(View):
    def get(self, request):

        articles = ArticleModel.objects.all()
        # articles = [
        #     {
        #         "title": "Python 5 is officially announced",
        #         "category": "tech",
        #         "author": "Guido van Rossum",
        #         "content": "Just joking, we will have Python 3 for some years",
        #         "creation_date": datetime.now()
        #     },
        #     {
        #         "title": "Tesla goes bankrupt",
        #         "category": "auto",
        #         "author": "Elon Musk",
        #         "content": "Just trying to increase Tesla share price here!",
        #         "creation_date": datetime.now()
        #     }
        # ]
        return render(request, "articles.html", {"articles": articles})
