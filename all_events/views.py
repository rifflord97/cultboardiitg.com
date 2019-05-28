from django.shortcuts import render
from home.models import Upcoming_Events


def events(request):
    event = Upcoming_Events.objects.all()
    context = {'event': event}
    return render(request, 'all_events.html', context)
