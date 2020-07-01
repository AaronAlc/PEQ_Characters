from django.urls import path

from characters import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/', views.detail, name='detail'),
]
