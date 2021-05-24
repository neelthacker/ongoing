from django.contrib import admin
from django.urls import path
from . import views


app_name = 'feedback'
urlpatterns = [ 
    path(r'feedback/', views.create_feedback, name='feedback'),
    path(r'feedback/<int:pk>/', views.update_feedback, name='feedback_update'),
    path(r'admin_permission/', views.admin_permission, name='admin_permission'),
    path(r'admin_permission/<int:pk>/', views.admin_permission1, name='admin_permission1'),
]