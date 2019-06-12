from django.urls import re_path
from . import views

app_name = 'clubs_montage'

urlpatterns = [
    re_path(r'', views.montage, name='clubs_montage'),
]
