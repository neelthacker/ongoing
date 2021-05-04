from django.contrib import admin
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [ 
    path(r'', views.post_list, name='home'),
    path(r'<slug:slug>/<int:page>', views.post_detail, name='post_detail'),
    path(r'createpost/', views.create_post, name='create'),
    path(r'updatepost/<slug:slug>/<int:page>', views.update_post, name='update'),
    path(r'delete/<slug:slug>/', views.delete_post, name='delete'),
    path(r'login/', views.log_in, name='login'),
    path(r'signup/', views.sign_up, name='signup'),
    path(r'logout/', views.log_out, name='logout'),
    path(r'user_list/', views.user_list, name='user_list'),
    path(r'category_list/', views.add_category, name='category'),
    path(r'ajax_search/', views.ajax_search, name='ajax_search'),
    path(r'ajax_category/', views.ajax_category, name='ajax_category'),
    path(r'<slug:slug>/comment', views.comment, name='comment'),
    path(r'comment_delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]