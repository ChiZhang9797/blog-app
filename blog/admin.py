from django.contrib import admin
from django.db import models

from mdeditor.widgets import MDEditorWidget

from .models import Post, PostImage

class PostImageAdmin(admin.StackedInline):
    extra = 0
    model = PostImage
    def image_url(self, obj):
        print(obj.image.url)
        return obj.image.url
    image_url.allow_tags = True
    readonly_fields = ('image_url',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget},
    }

    inlines = [PostImageAdmin]
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author') 
    search_fields = ('title', 'body') 
    prepopulated_fields = {'slug': ('title',)} 
    raw_id_fields = ('author',) 
    date_hierarchy = 'publish' 
    ordering = ('status', 'publish')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass