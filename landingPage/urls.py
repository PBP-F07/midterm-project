from django.urls import path
from landingPage.views import show_main, get_books_json, search_books, fetch_static_books
from wishlist_page.views import search_books

app_name = 'landingPage'

urlpatterns = [
    path(' ', show_main, name='show_main'),
    path('get_books/', get_books_json, name='get_books_json'),
    path('search_books/', search_books, name='search_books'),
]

fetch_static_books()
