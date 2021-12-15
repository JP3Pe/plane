from django.urls import path

from user import views

urlpatterns = [
    path('', views.UserLoginView.as_view()),
    path('login', views.UserLoginView.as_view(), name='log-in'),
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('logout', views.UserLogoutView.as_view(), name='log-out'),
]
