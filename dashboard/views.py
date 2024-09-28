from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from frontend.models import FAQModels
from .forms import FAQForm, DataInputForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DataInput
from django.urls import reverse_lazy
class DashboardIndex(TemplateView):
    template_name= 'dashboard/dashboard_index.html'
    

class UserInputView(CreateView):
    model = DataInput
    form_class = DataInputForm
    template_name = 'dashboard/input_create.html'
    success_url = reverse_lazy('dashboard:user_list')
    
    def form_valid(self, form):
        user = self.request.user  # Get the current user
        form.instance.user = user  # Assign the user to the DataInput instance
        form.save()  # Save the form data
        return super().form_valid(form) 
    
class InputList(ListView):
    model= DataInput
    template_name='dashboard/data_list.html'
    
    def get_context_data(self, **kwargs):
        personal_user=self.request.user
        context = super().get_context_data(**kwargs)
        context["items"] = DataInput.objects.filter(user=personal_user) 
        return context
    
    
    
    