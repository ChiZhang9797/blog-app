from os import name
from django.urls import path
from .views import BlogDetailView, BlogListView
from .feeds import LatestPostsFeed

urlpatterns = [
     path('', BlogListView.as_view(), name='home'),
     path('tag/<slug:tag_slug>/', BlogListView.as_view(), 
          name='post_list_by_tag'),
     path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
          BlogDetailView.as_view(), name='post_detail'),
     path('feed/',LatestPostsFeed(), name='post_feed'),
]
