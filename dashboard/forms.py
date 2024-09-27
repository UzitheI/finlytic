
from django import forms
from frontend.models import FAQModels


class FAQForm(forms.ModelForm):
    
    class Meta:
        model=FAQModels
        fields='__all__'