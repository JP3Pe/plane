from django.shortcuts import render, redirect

from trip.forms import TripForm
from trip.models import Trip


def get_posts(request):
    if request.method == 'GET':
        posts = Trip.objects.all()
        return render(request, 'board.html', {'posts': posts})


def create_posts(request):
    if request.method == 'GET':
        form = TripForm
        return render(request, 'board_write.html', {'form': form})
    elif request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = Trip(**form.cleaned_data)
            trip.save()
        return redirect('trips')
