from django.urls import path

from user import views

urlpatterns = [
    # TODO: Active links below
    path('', views.sign_in, name='sign-in'),
    path('sign-in', views.sign_in, name='sign-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    # path('logout', views.logout),
]
