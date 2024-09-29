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
from django.conf import settings
import requests
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import DataInput
from .forms import DataInputForm
from django.contrib.auth.models import User
from datetime import timezone
from datetime import datetime, date

from django.core.mail import send_mail

class DashboardIndex(ListView):
    model = User
    template_name = 'dashboard/dashboard_index.html'
    
    def get_context_data(self, **kwargs):
        personal_user = self.request.user
        context = super().get_context_data(**kwargs)
        
        today = date.today()
        # Set the target year to June 26, 2025, as per your request
        target_date = date(2024, 10, 1)
        
        # Calculate the difference in days between today and the target date
        date_diff = (target_date - today).days
    
        context["date_till_tax"] = date_diff
        
        context["items"] = DataInput.objects.filter(user=personal_user) 
        
        # Send an email if there are less than 10 days remaining
        if date_diff < 10:
            context["users_with_deadlines"] = True
            self.send_deadline_email(personal_user, date_diff)
        
        return context
    
    def send_deadline_email(self, user, days_left):
        personal_user=self.request.user
        subject = "Tax Deadline Alert: Less than 10 Days Left!"
        message = f"Dear Customer,\n\nThere are only {days_left} days left until the tax deadline on June 26, 2025. Please make sure to complete any pending tasks.\n\nBest regards,\nFinlytic"
        
        recipient_email = user.email
        
        # Send email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  
            [recipient_email], 
            fail_silently=False,
        )


    

class UserInputView(CreateView):
    model = DataInput
    form_class = DataInputForm
    template_name = 'dashboard/input_create.html'
    success_url = reverse_lazy('dashboard:user_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        data_input_instance = form.save()


        query = form.cleaned_data.get('query')
        print("Query from form:", query) 

        data = {
            'query': query,
        }

        try:
            excel_file = self.request.FILES['excel_file']  
            print("Excel file from form:", excel_file)  

            files = {
                'excel_file': excel_file, 
            }
            print("Files prepared for API call:", files)
        except KeyError:
            print("No 'excel_file' found in request.FILES.")
            form.add_error(None, "Excel file is required.")
            return self.form_invalid(form)
        
        api_key = 'Efx6Y9+UHkSIw5SRnGc1UAxcC8FUkb8VlrsQgsUkaoE='

        headers = {
            'Authorization': f'Bearer {api_key}',  
        }
        print("Headers prepared for API call:", headers)

        try:
            print("Sending request to API...")
            response = requests.post(
                'https://fin-qqqog.eastus2.inference.ml.azure.com/score',
                data=data, 
                files=files,  
                headers=headers,
                timeout=1000 
            )
            print("Received response from API:", response.status_code)
            response.raise_for_status()

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
    
    
    
