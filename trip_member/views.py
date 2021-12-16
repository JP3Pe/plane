from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View

from trip.models import Trip
from trip_member.models import TripMember


class TripMemberCreateView(View):
    @staticmethod
    def post(request, trip_id):
        if request.user.is_authenticated:
            trip = Trip.objects.filter(id=trip_id)[0]
            trip_member = TripMember()

            trip_member.member = User.objects.get(username=request.user.get_username())
            trip_member.trip = trip
            trip_member.save()

            #  TODO: 해당 게시글로 포워드
            return redirect('trips')

        else:
            return redirect('trips')
