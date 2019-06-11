from django.urls import re_path
from . import views

app_name = 'clubs_octaves'

urlpatterns = [
    re_path(r'', views.octaves, name='clubs_octaves'),
]
