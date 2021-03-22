"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sitemaps
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls.conf import re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic.base import RedirectView

from blog.sitemaps import PostSitemap

from pathlib import Path

import cloudinary
import os

BASE_DIR = Path(__file__).resolve().parent.parent

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
          name='django.contrib.sitemaps.views.sitemap'),
    re_path(r'^mdeditor/', include('mdeditor.urls'))
]

urlpatterns += [
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'static')
    })
]

# static files (images etc.)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
