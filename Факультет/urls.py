
from django.urls import path

from Факультет import views
from Факультет.views import index

urlpatterns = [
    path('', views.knu, name='index'),
    path('about/', views.knu, name='about'),
    path('parol/', views.parol, name='parol'),
]