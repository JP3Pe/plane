from django.urls import path

from trip import views

urlpatterns = [
    path('', views.get_posts, name='trips'),
    path('create', views.create_posts, name='create-post'),
]
