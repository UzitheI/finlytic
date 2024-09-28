
from django import forms
from frontend.models import FAQModels
from .models import DataInput


class FAQForm(forms.ModelForm):
    
    class Meta:
        model=FAQModels
        fields='__all__'

class DataInputForm(forms.ModelForm):
    class Meta:
        model=DataInput
        fields= ['excel_file','query']