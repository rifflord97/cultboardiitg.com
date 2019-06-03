from django.shortcuts import render
from .models import Links, Gallery


def manthan(request):
    images = Gallery.objects.all()
    link = Links.objects.all()
    context = {
        'images': images,
        'link': link,
    }
    return render(request, 'manthan.html', context)
