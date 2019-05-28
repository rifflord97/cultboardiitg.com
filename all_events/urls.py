from django.urls import path,re_path
from . import views

app_name = 'all_events'

urlpatterns = [
    re_path(r'', views.events, name='events'),
]
