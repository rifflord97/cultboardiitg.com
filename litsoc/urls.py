from django.urls import re_path
from . import views

app_name = 'clubs_litsoc'

urlpatterns = [
    re_path(r'', views.litsoc, name='clubs_litsoc'),
]
