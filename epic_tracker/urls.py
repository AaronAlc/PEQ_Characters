from django.urls import path
from . import views

urlpatterns = [
    path('', views.epic_dashboard, name='epic_dashboard'),
]