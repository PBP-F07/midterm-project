from django.urls import path
from landingPage.views import show_main, get_books_json, search_books, fetch_static_books

app_name = 'landingPage'

urlpatterns = [
    path('landingPage/', show_main, name='show_main'),
    path('get_books/', get_books_json, name='get_books_json'),
    path('search_books/', search_books, name='search_books'),
]

fetch_static_books()