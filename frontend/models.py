from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FAQModels(models.Model):
    question=models.CharField(max_length=150)
    answer=models.CharField (max_length=450)

class ContactModel(models.Model):
    name=models.CharField( max_length=150)
    email=models.EmailField(max_length=54)
    message=models.CharField(max_length=300)
    contact_number=models.IntegerField(blank=True, null=True)

class ChatModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.CharField(max_length=150)
    date_time=models.DateTimeField(auto_now_add=True)

class UserSummary(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    summary=models.CharField(max_length=800)
    date_time=models.DateTimeField(auto_now_add=False)
    
    
    