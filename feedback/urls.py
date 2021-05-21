from django.contrib import admin
from django.urls import path
from . import views


app_name = 'feedback'
urlpatterns = [ 
    path(r'feedback/', views.create_feedback, name='feedback'),
    path(r'feedback/<int:pk>/', views.update_feedback, name='feedback_update'),
]