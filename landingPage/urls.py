from django.urls import path
from landingPage.views import show_main, get_books_json, search_books_static, fetch_static_books, borrow_book, show_json_by_id
from wishlist_page.views import search_books

app_name = 'landingPage'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('get_books/', get_books_json, name='get_books_json'),
    path('search_books_static/', search_books_static, name='search_books_static'),
    path('borrow_book/<int:id>/', borrow_book, name='borrow_book'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]