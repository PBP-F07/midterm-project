import requests
import os
import json
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from landingPage.models import Books
from django.core import serializers
from user_profile_page.models import Member
from django.contrib.auth.decorators import login_required




# Create your views here.
counter = 0
def show_main(request):
    context = {
        'name': request.user.username
    }
    
    fetch_static_books()
    return render(request, "main.html", context)

def fetch_static_books():
    jsonFile = os.path.join(settings.STATIC_ROOT, 'admin/books_data.json')

    with open(jsonFile, 'r', encoding='utf-8') as books_data:
        books = json.load(books_data)

        for book in books:
            title = book.get('title')
            author_raw = book.get('authors', [])
            author = ', '.join(author_raw)
            description = book.get('description')
            image = book.get('cover_image')
            year_of_release = book.get('release_year')

            Books.objects.create(title=title, author=author, description=description, image=image, year_of_release=year_of_release)

    books_data.close()

def fetch_books(self): # untuk ngambil data langsung dari google api
    api_key = 'your_google_api_key'
    query = 'search_query_here'
    max_results = 100 

    url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}&maxResults={max_results}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            title = volume_info.get('title', '')
            author = ', '.join(volume_info.get('authors', []))
            description = volume_info.get('description', '')
            image_url = volume_info.get('imageLinks', {}).get('thumbnail', '')
            year_of_release = volume_info.get('publishedDate', '')

            Books.objects.create(
                title=title,
                author=author,
                description=description,
                image=image_url,
                year_of_release=year_of_release
            )

def get_books_json(request):
    books_item = Books.objects.all()
    return HttpResponse(serializers.serialize('json', books_item))


def lend_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    if book.borrowed_by:
        return HttpResponse("Book already borrowed!", status=400)
    book.borrowed_by = request.user
    book.save()
    return redirect('user_profile_page:user_dashboard')