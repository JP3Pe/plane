from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from schedule.forms import ScheduleForm
from schedule.models import Schedule
from trip.forms import TripForm
from trip.models import Trip


class PostListView(ListView):
    model = Trip
    context_object_name = 'post_list'
    template_name = 'board.html'


class PostCreateView(View):
    @staticmethod
    def get(request):
        trip_form = TripForm
        schedule_form = ScheduleForm
        return render(request, 'board_write.html', {'trip_form': trip_form, 'schedule_form': schedule_form})

    @staticmethod
    def post(request):
        if request.user.is_authenticated:
            trip_form = TripForm(request.POST)
            trip = None

            if trip_form.is_valid():
                trip = Trip(**trip_form.cleaned_data)
                trip.author = User.objects.get(username=request.user.get_username())
                trip.save()

            schedules = request.POST.getlist('place')
            for schedule in schedules:
                # TODO: Validation 추가
                Schedule.objects.create(trip=trip, place=schedule)

        else:
            return redirect('sign-in')

        return redirect('trips')
