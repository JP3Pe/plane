from django.urls import path

from user import views

urlpatterns = [
    # TODO: Active links below
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    # path('logout', views.logout, name='logout'),
]
