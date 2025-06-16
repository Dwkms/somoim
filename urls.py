# somoim_project/somoim/urls.py
from django.urls import path
from . import views

app_name = 'somoim'

urlpatterns = [
    path('', views.index, name='index'),
]