from django.urls import path
from . import views 

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view() , name='blog_list'),
    path('my-blogs', views.MyBlogs.as_view() , name='my_blogs'),
    path('write/', views.CreateBlog.as_view() , name='create_blog'),
    path('details/', views.blog_details , name='blog_details'),
    path('liked/<pk>', views.liked  , name='liked_post'),
    path('unliked/<pk>', views.unliked , name='unliked_post')
]
