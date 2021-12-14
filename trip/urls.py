from django.urls import path

from trip import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='trips'),
    path('create', views.create_posts, name='create-post'),
]
