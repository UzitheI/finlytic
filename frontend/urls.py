from django.urls import path
from .views import IndexView, ChatTemplate
app_name= "frontend"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chatbot/',ChatTemplate.as_view(),name='chatbot'),
]
