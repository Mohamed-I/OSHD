from django.urls import path, include
from .views import EmployeeView


urlpatterns = [
    path('', EmployeeView.as_view(), name='users'),
]
