from django.urls import re_path
from . import views

app_name = 'clubs_lumiere'

urlpatterns = [
    re_path(r'', views.lumiere, name='clubs_lumiere'),
]
