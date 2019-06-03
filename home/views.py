from django.shortcuts import render
from .models import About, Team, Upcoming_Events

def index(request):
    about = About.objects.get(pk=1)
    latest = Upcoming_Events.objects.all().order_by('-pk')[:4]
    team = Team.objects.all().order_by('-pk')[:3]
    team1 = team[0]
    team2 = team[1]
    team3 = team[2]
    event1 = latest[0]
    event2 = latest[1]
    event3 = latest[2]
    context = {
        'events': latest,
        'about': about,
        'team1': team1,
        'team2': team2,
        'team3': team3,
        'event1': event1,
        'event2': event2,
        'event3': event3,
    }
    return render(request,'homepage.html', context)