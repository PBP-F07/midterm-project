from django.urls import path
from wishlist_page.views import create_product_flutter, search_books, add_to_wishlist, load_wishlist, delete_item_ajax, show_json, add_book_ajax, create_notes, update_mood_ajax
from landingPage.views import get_books_json  

app_name = 'wishlist_page'

urlpatterns = [
    path(' ', search_books, name='search_books'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('load_wishlist/', load_wishlist, name='load_wishlist'),
    path('get_books_from_landing_page/', get_books_json, name='get_books_from_landing_page'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('json/', show_json, name='show_json'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('create-notes', create_notes, name='create_notes'),
    path('update-mood-ajax/', update_mood_ajax, name='update_mood_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]