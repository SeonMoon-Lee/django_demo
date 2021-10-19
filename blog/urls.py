from django.urls import path
from blog import views
urlpatterns = [
    path("home/", views.blog_home),
    path("create/", views.blog_create),
    path("post/", views.blog_post),
]
