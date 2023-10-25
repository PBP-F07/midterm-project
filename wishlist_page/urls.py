from django.urls import path
from wishlist_page.views import search_books, add_to_wishlist, load_wishlist

app_name = 'wishlist_page'

urlpatterns = [
    path(' ', search_books, name='search_books'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('load_wishlist/', load_wishlist, name='load_wishlist'),
    
]