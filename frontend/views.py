from django.shortcuts import render
from django.views.generic import CreateView,TemplateView, DetailView
# Create your views here
from frontend.models import ContactModel 
from .forms import ContactForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
class IndexView(CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = 'frontend/index.html'
    success_url = reverse_lazy('frontend:index')

    def form_valid(self, form):
        form.save()  # Save the form data
        return super().form_valid(form)  # Call the parent's form_valid method

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # No need to add the form again; it's already part of the context
        return context