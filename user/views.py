from django.shortcuts import render
from django.views import generic
from .models import Employee


class EmployeeView(generic.ListView):
    model = Employee
    template_name = 'home.html'

