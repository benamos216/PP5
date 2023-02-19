from django.urls import path
from . import views


urlpatterns = [
    path('', views.review, name='review'),
    path('review/', views.add_review, name='add_review'),
    # path('approve_review/<int:review_id>/', views.approve_review, name='approve_review'),
    path('delete/<int:review_id>', views.delete_review, name='delete_review'),
]
