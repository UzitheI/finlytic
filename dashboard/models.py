from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class DataInput(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    excel_file = models.FileField(upload_to='excel_files/')
    query=models.CharField(max_length=250)
    sent_date=models.DateField(auto_now=True)
