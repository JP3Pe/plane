from django.urls import path

from trip import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='trips'),
    path('create', views.PostCreateView.as_view(), name='create-post'),
    path('detail/<int:trip_id>', views.PostDetailView.as_view(), name='detail-post')
]
