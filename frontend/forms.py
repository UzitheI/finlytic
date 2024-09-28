from django import forms
from .models import ContactModel, ChatModel
class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = '__all__'

class ChatInput(forms.ModelForm):
    
    class Meta:
        model= ChatModel
        fields= ['question']