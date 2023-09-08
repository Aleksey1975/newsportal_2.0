from django.urls import path
from .views import *



urlpatterns = [

    path('', ListPost.as_view(), name='index'),
    path('news/search/', ListNews.as_view(), name='news'),
    path('news/', ListNewsOnly.as_view(), name='news_only'),
    path('articles/', ListArticles.as_view(), name='articles'),
    path('news/<int:pk>/', DetailNews.as_view(), name='one_news'),
    path('article/<int:pk>/', DetailArticle.as_view(), name='one_article'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='news_edit'),
    path('article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),


    path('comments/', comments, name='comments'),
    path('showcomment/<int:comment_id>', showcomment, name='showcomment'),
    path('showpost/<int:post_id>', showpost, name='showpost'),

    path('like-news/<int:post_id>', like_news, name='like-news'),
    path('dislike-news/<int:post_id>', dislike_news, name='dislike-news'),
    path('like-article/<int:post_id>', like_article, name='like_article'),
    path('dislike-article/<int:post_id>', dislike_article, name='dislike_article'),
    path('like-comment/<int:comment_id>', like_comment, name='like-comment'),
    path('dislike-comment/<int:comment_id>', dislike_comment, name='dislike-comment'),

]
