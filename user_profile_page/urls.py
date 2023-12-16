from django.urls import path
from . import views
from user_profile_page.views import load_wishlist, get_borrowed_books_json, get_wishlisted_books_json, delete_all_books, show_json_by_id, show_json, show_json_books, show_json_books_by_id, get_user_profile_json, fetch_username, get_books, return_book_flutter, show_json_wishlist

app_name = 'user_profile_page'

urlpatterns = [
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('update-bio-ajax/', views.update_bio_ajax, name='update_bio_ajax'),
    path('load_wishlist/', load_wishlist, name='load_wishlist'),
    path('load-borrowed-book/', views.load_borrowed_book, name='load_wishlist'),
    path('borrowed_book_check_render/', views.borrowed_book_check_render, name='borrowed_book_check_render'),
    path('return_book/<int:id>/', views.return_book, name='return_book'),
    path('get_borrowed_books_json/', get_borrowed_books_json, name='get_borrowed_books_json'),
    path('get_wishlisted_books_json/', get_wishlisted_books_json, name='get_wishlisted_books_json'),
    path('delete_all_books/', delete_all_books, name='delete_all_books'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('json/', show_json, name='show_json'),
    path('return-book-flutter/<int:id>/', return_book_flutter, name='return_book_flutter'),
    path('json-books/', show_json_books, name='show_json'),
    path('json-wishlist/', show_json_wishlist, name='show_json_wishlist'),
    path('json-books/<int:id>/', show_json_books_by_id, name='show_json'),
    path('get-user-profile-json/', get_user_profile_json, name='get_user_item_json'),
    path('fetch-username/', fetch_username, name='fetch_username'),
    path('get-books/', get_books, name='get_books'),

]