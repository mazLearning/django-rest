from django.urls import path
from .views import ArticleList, ArticleDetail

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article-detail/<slug:slug>', ArticleDetail.as_view(), name='article_detail')
]
