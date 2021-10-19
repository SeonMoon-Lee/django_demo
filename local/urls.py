from django.urls import path
from local import views
urlpatterns = [
    path("local_shops/", views.local_shops),
]