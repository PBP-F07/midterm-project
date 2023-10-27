import requests
import os
import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from landingPage.models import Books
from django.core import serializers

# Create your views here.
counter = 0
def show_main(request):
    context = {
        'name': request.user.username
    }
    
    return render(request, "main.html", context)

def fetch_static_books():
    jsonFile = os.path.join(settings.STATIC_ROOT, 'admin/books_data.json')

    with open(jsonFile, 'r', encoding='utf-8') as books_data:
        books = json.load(books_data)

        jsonAmount = len(books)
        dbAmount = Books.objects.count()

        if jsonAmount <= dbAmount:
            books_data.close()
            return

        for book in books:
            title = book.get('title')
            author_raw = book.get('authors', [])
            author = ', '.join(author_raw)
            description = book.get('description')
            image = book.get('cover_image')
            year_of_release = book.get('release_year')
            amount = 5

            Books.objects.create(
                title=title, 
                author=author, 
                description=description, 
                image=image, 
                year_of_release=year_of_release, 
                amount=amount
            )

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
                year_of_release=year_of_release,
                amount=5
            )

def get_books_json(request):
    books_item = Books.objects.all()
    return HttpResponse(serializers.serialize('json', books_item))

def search_books(request):
    search_title = request.GET.get('search_title', '')

    # Query the database
    books_item = Books.objects.filter(title__icontains=search_title)

    return HttpResponse(serializers.serialize('json', books_item))

    """
    if request.is_ajax():
        return JsonResponse(data)
    else:
        return render(request, 'book_search_results_ajax.html', {'data': data})
    """