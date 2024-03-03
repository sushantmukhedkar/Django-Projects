# mis_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Department, Employee, Project

def chart_data(request):
    department_count = Department.objects.count()
    employee_count = Employee.objects.count()
    project_count = Project.objects.count()

    data = {
        'labels': ['Departments', 'Employees', 'Projects'],
        'datasets': [{
            'label': 'Count',
            'backgroundColor': ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
            'borderColor': ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)'],
            'borderWidth': 1,
            'data': [department_count, employee_count, project_count],
        }]
    }

    return JsonResponse(data)

def dashboard(request):
    return render(request, 'dashboard.html')