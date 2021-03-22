from django.contrib import admin
from django.db import models

from mdeditor.widgets import MDEditorWidget

from .models import About

@admin.register(About)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget},
    }