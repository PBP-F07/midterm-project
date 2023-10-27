from django.urls import path
from landingPage.views import show_main, get_books_json, borrow_book
from wishlist_page.views import search_books

app_name = 'landingPage'

urlpatterns = [
    path(' ', show_main, name='show_main'),
    path('get_books/', get_books_json, name='get_books_json'),
    path('borrow_book/<str:book_title>/', borrow_book, name='borrow_book'),
]