from django.shortcuts import render
from .models import Club_sec, Youtube, Gallery, Club_Member, Acheivement, Imp_Link


def cadence(request):
    secy = Club_sec.objects.all()
    images = Gallery.objects.all()
    videos = Youtube.objects.all()
    members = Club_Member.objects.all()
    acheivements = Acheivement.objects.all()
    links = Imp_Link.objects.all()
    context = {
        'secy': secy,
        'images': images,
        'videos': videos,
        'memb': members,
        'acheivements': acheivements,
        'links': links,


    }
    return render(request, 'cadence.html', context)

