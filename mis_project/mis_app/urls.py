# mis_app/urls.py
from django.urls import path
from .views import chart_data, dashboard

urlpatterns = [
    path('chart-data/', chart_data, name='chart_data'),
    path('dashboard/', dashboard, name='dashboard'),
    
]
