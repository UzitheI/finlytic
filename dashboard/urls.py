from django.urls import path
from .views import DashboardIndex, UserInputView, InputList

app_name= "dashboard"
urlpatterns = [
    path('', DashboardIndex.as_view(), name='dashboard'),
    path('user_input/', UserInputView.as_view(), name='user_input'),
    path('user_input_list/', InputList.as_view(), name='user_list'),
]
