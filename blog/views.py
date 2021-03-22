from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.db.models import Q, query

from taggit.models import Tag

from .models import Post

class BlogListView(ListView):
    paginate_by = 5
    template_name = "home.html"
    context_object_name = "post_list"

    # def get(self, request, tag_slug=None):
    #     post_list = Post.published.all()
    #     tag = None

    #     if tag_slug:
    #         tag = get_object_or_404(Tag, slug=tag_slug)
    #         post_list = post_list.filter(tags__in=[tag])

    #     strval = request.GET.get("search", False)
    #     if strval:
    #         query = Q(title__icontains=strval)
    #         query.add(Q(test__icontains=strval), Q.OR)
    #         post_list = Post.published.filter(query).select_related()

    #     ctx = {'post_list': post_list, 'tag': tag, 'search': strval}

    #     return render(request, self.template_name, ctx)
        
    def get_queryset(self):
        post_list = Post.published.all()
        self.tag = None

        if 'tag_slug' in self.kwargs:
            self.tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            post_list = post_list.filter(tags__in=[self.tag])

        self.strval = self.request.GET.get("search", False)
        if self.strval:
            query = Q(title__icontains=self.strval)
            query.add(Q(body__icontains=self.strval), Q.OR)
            post_list = Post.published.filter(query).select_related()

        return post_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        context['search'] = self.strval
        return context

class BlogDetailView(DetailView):
    template_name = "post_detail.html"
    queryset = Post.published.all()
    context_object_name = "post"

    def get_object(self):
        post = get_object_or_404(Post, slug=self.kwargs['post'],
                                       status='published',
                                       publish__year=self.kwargs['year'],
                                       publish__month=self.kwargs['month'],
                                       publish__day=self.kwargs['day'],)

        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['post'] = post
        return context