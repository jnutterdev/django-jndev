from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'layouts/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'layouts/post_detail.html'