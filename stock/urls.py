from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_stocks, name='stocks'),
    path('<int:stock_id>/', views.stock_detail, name='stock_detail'),
]