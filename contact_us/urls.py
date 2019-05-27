from django.urls import path,re_path
from . import views

app_name = 'contact'

urlpatterns = [
    re_path(r'', views.contact, name='contact'),
]
