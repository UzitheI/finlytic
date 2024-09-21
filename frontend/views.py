from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name= 'frontend/index.html'