from django.shortcuts import render

from trip.models import Trip


def get_posts(request):
    if request.method == 'GET':
        posts = Trip.objects.all()
        return render(request, 'board.html', {'posts': posts})
