from django.shortcuts import render
from .models import About, Team, Upcoming_Events

def index(request):
    about = About.objects.get(pk=1)
    latest = Upcoming_Events.objects.filter(since='29/03/17').order_by('-id')[:10]
    team1 = latest.get(pk=1)
    team2 = latest.get(pk=2)
    team3 = latest.get(pk=3)
    event1 = Upcoming_Events.objects.get(pk=1)
    event2 = Upcoming_Events.objects.get(pk=2)
    event3 = Upcoming_Events.objects.get(pk=3)
    context = {
        'about': about,
        'team1': team1,
        'team2': team2,
        'team3': team3,
        'event1': event1,
        'event2': event2,
        'event3': event3,
    }
    return render(request,'home/homepage.html', context)