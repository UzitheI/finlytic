from django.db import models

# Create your models here.

class FAQModels(models.Model):
    question=models.CharField(max_length=150)
    answer=models.CharField (max_length=450)

class ContactModel(models.Model):
    name=models.CharField( max_length=150)
    email=models.EmailField(max_length=54)
    message=models.CharField(max_length=300)
    contact_number=models.IntegerField(blank=True, null=True)

