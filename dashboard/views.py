from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from frontend.models import FAQModels
from .forms import FAQForm, DataInputForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import DataInput
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import requests
class DashboardIndex(TemplateView):
    template_name= 'dashboard/dashboard_index.html'

import json
import requests
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class UserInputView(CreateView):
    model = DataInput
    form_class = DataInputForm
    template_name = 'dashboard/input_create.html'
    success_url = reverse_lazy('dashboard:user_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        data_input_instance = form.save()

        # Prepare the data for the API call
        data = {
            'query': form.cleaned_data.get('query'),  # Send other form fields as JSON
        }

        # Prepare the files for the API call
        files = {
            'excel_file': self.request.FILES['excel_file'],  # Send file separately
        }

        # API key (replace this with your actual key)
        api_key = 'Efx6Y9+UHkSIw5SRnGc1UAxcC8FUkb8VlrsQgsUkaoE='

        # Prepare the headers with the API key for authentication
        headers = {
            'Authorization': f'Bearer {api_key}',  # Add the key to the Authorization header
            'Content-Type': 'multipart/form-data',  # Content-Type for file upload
        }

        try:
            # Make the API request
            response = requests.post(
                'https://finlytic-models-hhgwg.southindia.inference.ml.azure.com/score',
                data=data,  # Form data
                files=files,  # Files
                headers=headers  # Authentication headers
            )
            response.raise_for_status()

            # Handle the response data
            api_response_data = response.json()

        except requests.exceptions.RequestException as e:
            form.add_error(None, f"An error occurred while sending data: {e}")
            return self.form_invalid(form)

        return super().form_valid(form)

    
class InputList(ListView):
    model= DataInput
    template_name='dashboard/data_list.html'
    
    def get_context_data(self, **kwargs):
        personal_user=self.request.user
        context = super().get_context_data(**kwargs)
        context["items"] = DataInput.objects.filter(user=personal_user) 
        return context
    
    
    
    