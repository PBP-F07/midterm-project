from django.urls import path
from wishlist_page.views import search_books, add_to_wishlist, load_wishlist, delete_item_ajax, get_book_status, show_json
from landingPage.views import get_books_json  

app_name = 'wishlist_page'

urlpatterns = [
    path(' ', search_books, name='search_books'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('load_wishlist/', load_wishlist, name='load_wishlist'),
    path('get_books_from_landing_page/', get_books_json, name='get_books_from_landing_page'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('get_book_status/', get_book_status, name='get_book_status'),
    path('json/', show_json, name='show_json'),
]