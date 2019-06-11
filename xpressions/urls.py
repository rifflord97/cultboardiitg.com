from django.urls import re_path
from . import views

app_name = 'clubs_xpressions'

urlpatterns = [
    re_path(r'', views.xpressions, name='clubs_xpressions'),
]

