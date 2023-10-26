from django.urls import path
from wishlist_page.views import wishlist

app_name = 'wishlist_page'

urlpatterns = [
    path('', wishlist, name='main_views'),
]