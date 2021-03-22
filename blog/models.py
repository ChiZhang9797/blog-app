from django.db import models
from django.utils import timezone
from django.urls import reverse

from taggit.managers import TaggableManager

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

def post_folder(instance, filename):
    return 'images/{0}/{1}'.format(instance.post.slug, filename)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICE = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique_for_date='publish')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    introduction = models.CharField(max_length=225)
    body = models.TextField()   
    image = models.ImageField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft',)
    objects = models.Manager() # The default manager
    published = PublishedManager() # Custom manager
    tags = TaggableManager()
    
    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.publish.year,
                                            self.publish.month,
                                            self.publish.day,
                                            self.slug])
    @property
    def body_html(self):
        return generate_rich_content(self.body)

    def __str__(self) -> str:
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=post_folder, blank=True)

    def __str__(self) -> str:
        return self.post.title