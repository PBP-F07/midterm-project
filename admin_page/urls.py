from django.urls import path
from .views import show_main

app_name = 'admin_page'

urlpatterns = [
    path('', show_main, name='show_main'),
]