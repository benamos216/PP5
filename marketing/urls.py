from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
