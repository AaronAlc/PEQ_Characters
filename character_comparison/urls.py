from django.urls import path, re_path
from . import views

app_name = 'character_comparison'
urlpatterns = [
    path('', views.comparison_home, name='comparison_home'),
    re_path(r'search/?$', views.comparison_search, name='comparison_search'),
]
