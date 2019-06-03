from django.urls import re_path
from . import views

app_name = 'manthan'

urlpatterns = [
    re_path(r'', views.manthan, name='manthan'),
]
