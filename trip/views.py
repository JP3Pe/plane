from django.shortcuts import render, redirect

from schedule.forms import ScheduleForm
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
        trip_form = TripForm(request.POST)
        if trip_form.is_valid():
            trip = Trip(**trip_form.cleaned_data)
            trip.save()
        return redirect('trips')
