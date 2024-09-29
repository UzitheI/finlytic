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

import json
import requests
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

import requests
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import DataInput
from .forms import DataInputForm
from django.contrib.auth.models import User
from datetime import timezone
from datetime import datetime, date

class DashboardIndex(ListView):
    model = User
    template_name = 'dashboard/dashboard_index.html'
    
    def get_context_data(self, **kwargs):
        personal_user=self.request.user
        context = super().get_context_data(**kwargs)
        
        # Get today's date
        today = date.today()
        
        # Determine if we should use the next year for June 30
        if today > date(today.year, 6, 30):
            target_year = today.year + 1  # Next year if past June 30 this year
        else:
            target_year = today.year  # This year if before or on June 30
        
        # Set June 30 of the determined target year
        june_30_next_year = date(target_year, 6, 30)
        
        # Calculate the difference in days between today and June 30 of next year
        date_diff = (june_30_next_year - today).days
        
        # Add the difference to the context
        context["date_till_tax"] = date_diff
        
        # Create a 'users_with_deadlines' context variable that is True if date_diff is less than 10
        context["users_with_deadlines"] = date_diff < 10
        
        context["items"] = DataInput.objects.filter(user=personal_user) 
        
        return context

    

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
        query = form.cleaned_data.get('query')
        print("Query from form:", query)  # Check if the query is retrieved correctly

        data = {
            'query': query,  # Send other form fields as JSON
        }

        # Prepare the files for the API call
        try:
            excel_file = self.request.FILES['excel_file']  # Get the file from the request
            print("Excel file from form:", excel_file)  # Check if the file is retrieved correctly

            files = {
                'excel_file': excel_file,  # Send file separately
            }
            print("Files prepared for API call:", files)
        except KeyError:
            print("No 'excel_file' found in request.FILES.")
            form.add_error(None, "Excel file is required.")
            return self.form_invalid(form)

        # API key (replace this with your actual key)
        api_key = 'Efx6Y9+UHkSIw5SRnGc1UAxcC8FUkb8VlrsQgsUkaoE='

        # Prepare the headers with the API key for authentication
        headers = {
            'Authorization': f'Bearer {api_key}',  # Add the key to the Authorization header
            # Note: 'Content-Type' is usually set by requests when sending files
        }
        print("Headers prepared for API call:", headers)

        try:
            # Make the API request
            print("Sending request to API...")
            response = requests.post(
                'https://fin-qqqog.eastus2.inference.ml.azure.com/score',
                data=data,  # Form data
                files=files,  # Files
                headers=headers, # Authentication headers
                timeout=1000 
            )
            print("Received response from API:", response.status_code)
            response.raise_for_status()  # Raise an error for bad responses

            # Handle the response data
            api_response_data = response.json()
            print("API response data:", api_response_data)

        except requests.exceptions.RequestException as e:
            print("RequestException caught:", e)
            form.add_error(None, f"An error occurred while sending data: {e}")
            return self.form_invalid(form)

        print("Form is valid. Proceeding to the next step.")
        return super().form_valid(form)


    
class InputList(ListView):
    model= DataInput
    template_name='dashboard/data_list.html'
    
    def get_context_data(self, **kwargs):
        personal_user=self.request.user
        context = super().get_context_data(**kwargs)
        context["items"] = DataInput.objects.filter(user=personal_user) 
        return context
    
    
    
