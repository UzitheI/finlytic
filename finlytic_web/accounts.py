from allauth.account.views import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomSignupView(SignupView):
    def get_success_url(self):
        return reverse("account_login")