from django.urls import re_path
from . import views

app_name = 'clubs_debsoc'

urlpatterns = [
    re_path(r'', views.debsoc, name='clubs_debsoc'),
]
