# from django.shortcuts import render
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post#, Category, Author
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-date_time_in'
    template_name = 'news.html'
    context_object_name = 'news'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = PostFilter(self.request.GET, queryset)
#         return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['fresh_news'] = None
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'new_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['fresh_news'] = None
        return context

