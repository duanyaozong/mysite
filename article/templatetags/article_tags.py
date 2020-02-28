# -*- utf-8 -*-
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from article.models import ArticlePost
import markdown

register = template.Library()


@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article.count()


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):  # 最新发布的文章
    latest_articles = ArticlePost.objects.order_by('-created')[:n]
    return {'latest_articles': latest_articles}


@register.simple_tag
def most_commented_articles(n=3):  # 评论最多
    return ArticlePost.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:n]


@register.filter(name='markdown')  # 模板选择器，改名
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))
