from django.shortcuts import render
from .models import GenSec, Ev_Manager, Events_Team, Club_Secy, Chairman

def team(request):
    gs = GenSec.objects.all().order_by('-pk')[:1]
    gs_current = gs[0]
    em = Ev_Manager.objects.all().order_by('-pk')[:1]
    em_current = em[0]
    ev_team = Events_Team.objects.all()
    chr = Chairman.objects.all().order_by('-pk')[:1]
    chr_current = chr[0]
    clb = Club_Secy.objects.all()
    context = {
        'gs': gs_current,
        'em': em_current,
        'chr': chr_current,
        'ev_team': ev_team,
        'clb': clb,
    }
    return render(request, 'team.html', context)