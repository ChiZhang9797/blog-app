from django import template
from django.utils.safestring import mark_safe
from taggit.models import Tag
from blog.models import Post

import markdown

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@ register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('tag_list.html')
def show_all_tags():
    tag_list = Tag.objects.all()
    return {'tag_list': tag_list}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(
        text,
        extensions=['extra','codehilite',],
        extension_configs={
            'codehilite': [('css_class', 'highlight')]
        },
        output_format='html5'
        ))
