from django.urls import path

from trip import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='trips'),
    path('create', views.PostCreateView.as_view(), name='create-post'),
]
