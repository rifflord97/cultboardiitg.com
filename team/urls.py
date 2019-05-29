from django.urls import re_path
from . import views

app_name = 'team'


urlpatterns = [
    re_path(r'', views.team, name='team'),
]
