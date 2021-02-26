from django.contrib import admin
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [ 
    path(r'', views.post_list, name='home'),
    path(r'<slug:slug>/$', views.post_detail, name='post_detail'),
    path(r'createpost/', views.create_post, name='create'),
    path(r'updatepost/<slug:slug>/$', views.update_post, name='update'),
    path(r'delete/<slug:slug>/$', views.delete_post, name='delete'),
    path(r'login/', views.log_in, name='login'),
    path(r'signup/', views.sign_up, name='signup'),
    path(r'logout/', views.log_out, name='logout'),
    path(r'user_list/', views.user_list, name='user_list'),
    path(r'category_list/', views.add_category, name='category'),
    

    # path(r'<search:search>/$', views.search_blog, name='search_blog'),
]