from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.

class ArticleList(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.get_article_publish()


class ArticleDetail(DetailView):
    template_name = 'blog/article-detail.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Article.objects.get_article_by_slug(slug)