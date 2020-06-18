from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_home, name='character_home'),
    path('<str:name>/', views.character_detail, name='character_detail'),
]
