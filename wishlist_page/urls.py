from django.urls import path
from wishlist_page.views import show_main

app_name = 'wishlist_page'

urlpatterns = [
    path('', show_main, name='show_main'),
]