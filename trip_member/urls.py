from django.urls import path

from trip_member import views

urlpatterns = [
    path('create/<int:trip_id>', views.TripMemberCreateView.as_view(), name='create-trip-member')
]
