from django.urls import path
from .views import show_main, get_wishlist_json, show_json, reject_wishlist, add_catalog, get_allbooks_json, show_userpage, show_managebooks, get_book_by_title, delete_book, show_notes, get_allusers_mobile

app_name = 'admin_page'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('users/', show_userpage, name='show_userpage'),
    path('managebooks/', show_managebooks, name='show_managebooks'),
    path('json/', show_json, name='show_json'),
    path('show_notes/', show_notes, name='show_notes'),
    path('get-wishlist/', get_wishlist_json, name='get_wishlist_json'),
    path('get-allbooks/', get_allbooks_json, name='get_allbooks_json'),
    path('get-book-by-title/', get_book_by_title, name='get_book_by_title'),
    path('reject-wishlist/<int:id>', reject_wishlist, name='reject_wishlist'),
    path('add-catalog/<int:id>', add_catalog, name='add_catalog'),
    path('managebooks/delete-book/<int:id>', delete_book, name='delete_book'),
    path('get-allusers/', get_allusers_mobile, name='get_allusers')
]