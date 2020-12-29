from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyek/', views.proyek, name='proyek'),
    path('rutin/', views.rutin, name='rutin')
]