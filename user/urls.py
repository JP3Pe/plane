from django.urls import path

from user import views

urlpatterns = [
    # TODO: Active links below
    path('', views.sign_in, name='signin'),
    path('signup', views.sign_up, name='signup'),
    path('signin', views.sign_in, name='signin'),
    # path('logout', views.logout, name='logout'),
]
