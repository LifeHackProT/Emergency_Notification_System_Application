from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alarm/', views.alarm, name='alarm'),
    path('createform/', views.createform, name='createform'),
]