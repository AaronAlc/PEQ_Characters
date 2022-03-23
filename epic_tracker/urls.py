from django.urls import path
from . import views

app_name = 'epic_tracker'
urlpatterns = [
    path('', views.epic_dashboard, name='epic_dashboard'),
]