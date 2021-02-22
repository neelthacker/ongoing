from django.contrib import admin
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [ 
    path(r'', views.postlist, name='home'),
    path(r'<slug:slug>/$', views.postdetail, name='post_detail'),
    path(r'createpost', views.create_post,name='create'),
]