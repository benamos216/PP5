from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_stocks, name='stocks'),
    path('<int:stock_id>/', views.stock_detail, name='stock_detail'),
    path('add/', views.add_stock, name='add_stock'),
    path('edit/<int:stock_id>', views.edit_stock, name='edit_stock'),
    path('delete/<int:stock_id>', views.delete_stock, name='delete_stock'),
]
