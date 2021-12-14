from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from schedule.forms import ScheduleForm
from schedule.models import Schedule
from trip.forms import TripForm
from trip.models import Trip


def get_posts(request):
    if request.method == 'GET':
        posts = Trip.objects.all()
        return render(request, 'board.html', {'posts': posts})


def create_posts(request):
    if request.method == 'GET':
        trip_form = TripForm
        schedule_form = ScheduleForm
        return render(request, 'board_write.html', {'trip_form': trip_form, 'schedule_form': schedule_form})

    elif request.method == 'POST':
        if request.user.is_authenticated:
            trip_form = TripForm(request.POST)
            schedule_form = ScheduleForm(request.POST)
            trip = None

            if trip_form.is_valid():
                trip = Trip(**trip_form.cleaned_data)
                trip.author = User.objects.get(username=request.user.get_username())
                trip.save()

            if schedule_form.is_valid():
                schedule = Schedule(**schedule_form.cleaned_data)
                schedule.trip = trip
                schedule.save()

        else:
            return redirect('sign-in')

        return redirect('trips')
