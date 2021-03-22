from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.utils.feedgenerator import Rss201rev2Feed

from .models import Post

import re

class ExtendedRssFeed(Rss201rev2Feed):
    """Rss feed with content
    """
    def root_attributes(self):
        attrs = super().root_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        return attrs

    def add_item_elements(self, handler, item):
        super().add_item_elements(handler, item)
        handler.addQuickElement(u'content:encoded', item['content_encoded'])

class LatestPostsFeed(Feed):
    feed_type = ExtendedRssFeed
    title = 'Chi\'s blog'
    link = reverse_lazy('home')
    description = 'New posts of Chi\'s blog.'

    def items(self):
        return Post.published.all()[:3]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.introduction

    def item_link(self, item):
        return item.get_absolute_url()

    def feed_copyright(self):
        return "Copyright© 2018 Chi\'s Blog"
    
    def item_extra_kwargs(self, item):
        return {'content_encoded': self.item_content_encoded(item)}

    def item_content_encoded(self, item):
        html = item.body_html
        return html