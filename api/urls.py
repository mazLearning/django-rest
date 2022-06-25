from django.urls import path
from .views import (
    UserListAndCreate,
    UserDelete,
    UserUpdate,
    ArticleList,
    ArticleCreate,
    ArticleUpdate,
    ArticleDelete,
    # RevokeToken
)

app_name = 'api'
urlpatterns = [
    path('user-list', UserListAndCreate.as_view(), name='user_list'),
    path('user-update/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('user-delete/<int:pk>', UserDelete.as_view(), name='user_delete'),
    path('article-list', ArticleList.as_view(), name='article_list'),
    path('article-create', ArticleCreate.as_view(), name='article_create'),
    path('article-update/<int:pk>', ArticleUpdate.as_view(), name='article_update'),
    path('article-delete/<int:pk>', ArticleDelete.as_view(), name='article_delete'),
    # path('revoke-token', RevokeToken.as_view(), name='revoke_token')
]
