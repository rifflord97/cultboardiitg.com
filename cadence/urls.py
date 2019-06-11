from django.urls import re_path
from . import views

app_name = 'clubs_cadence'

urlpatterns = [
    re_path(r'', views.cadence, name='clubs_cadence'),
]
