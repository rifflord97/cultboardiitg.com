from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.template.loader import render_to_string
from home.models import Team


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST["name"]
        email = request.POST["email"]

        context = {'name' : name, 'email': email, 'message': message}
        email_template = render_to_string('./email_template.txt', context)

        send_mail(
            'Contact Form',
            email_template,
            settings.EMAIL_HOST_USER,
            ['cultboardiitg@gmail.com'],
            fail_silently=False
        )
        #return redirect('contact:received')

    team = Team.objects.all().order_by('pk')[:3]
    team1 = team[0]
    team2 = team[1]
    team3 = team[2]
    context = {
        'team1': team1,
        'team2': team2,
        'team3': team3,
    }
    return render(request, 'contact.html', context)

def received(request):
    return render(request, 'received.html', context)