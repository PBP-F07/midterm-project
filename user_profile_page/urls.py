from django.urls import path
from . import views
from user_profile_page.views import load_wishlist, get_borrowed_books_json, get_wishlisted_books_json

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
]