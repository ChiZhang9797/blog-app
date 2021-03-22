from django.db import models
from django.urls import reverse
from django.utils import timezone

import markdown

def generate_rich_content(text):
    return markdown.markdown(
        text,
        extensions=['extra','codehilite',],
        extension_configs={
            'codehilite': [('css_class', 'highlight')]
        },
        output_format='html5'
    )

# Create your models here.
class About(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='about_page'
    )
    update = models.DateTimeField(auto_now=True)

    @property
    def body_html(self):
        return generate_rich_content(self.body)

    def __str__(self):
        return "about"

    def get_absolute_url(self):
        return reverse("about")