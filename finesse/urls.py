from django.urls import re_path
from . import views

app_name = 'clubs_finesse'

urlpatterns = [
    re_path(r'', views.finesse, name='clubs_finesse'),
]
