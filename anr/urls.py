from django.urls import re_path
from . import views

app_name = 'clubs_anr'

urlpatterns = [
    re_path(r'', views.anr, name='clubs_anr'),
]
