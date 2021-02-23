from django.contrib import admin
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [ 
    path(r'', views.post_list, name='home'),
    path(r'<slug:slug>/$', views.post_detail, name='post_detail'),
    path(r'createpost', views.create_post,name='create'),
    path(r'login/', views.log_in, name='login'),
    path(r'signup/', views.sign_up, name='signup'),
    path(r'logout/', views.log_out, name='logout'),
]