from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from frontend.models import FAQModels
from .forms import FAQForm
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardIndex(TemplateView):
    template_name= 'dashboard/dashboard_index.html'
    
    