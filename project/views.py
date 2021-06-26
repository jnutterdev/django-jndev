from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'layouts/home.html'

class AboutPageView(TemplateView):
    template_name = 'layouts/about.html'

