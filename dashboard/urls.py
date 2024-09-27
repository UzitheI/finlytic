from django.urls import path
from .views import DashboardIndex

app_name= "dashboard"
urlpatterns = [
    path('', DashboardIndex.as_view(), name='dashboard'),
]
