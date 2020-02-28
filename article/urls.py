# -*- utf-8 -*-
from django.urls import path, re_path
from . import views, list_views


app_name = 'article'
urlpatterns = [
    path('article-column/', views.article_column, name='article_column'),
    path('rename-column/', views.rename_article_column, name='rename_article_column'),
    path('del-column/', views.del_article_column, name='del_article_column'),
    path('article-post/', views.article_post, name='article_post'),
    path('article-list/', views.article_list, name='article_list'),
    re_path(r'article-detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.article_detail, name='article_detail'),
    path('del-article/', views.del_article, name='del_article'),
    re_path(r'redit_article/(?P<article_id>\d+)/$', views.redit_article, name="redit_article"),
    path('list-article-titles/', list_views.article_titles, name='article_titles'),
    re_path(r'list-article-content/(?P<id>\d+)/(?P<slug>[-\w]+)/$', list_views.article_content,
            name='list_article_content'),
    re_path(r'list-article-titles/(?P<username>[-\w]+)/$', list_views.article_titles, name='author_articles'),
    path('like-article/', list_views.like_article, name='like_article'),
    path('article-tag/', views.article_tag, name='article_tag'),
    path('del-article-tag/', views.del_article_tag, name='del_article_tag')
]
