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
from django.views.decorators.csrf import csrf_exempt
from datetime import date

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

def search_books_static(request):
    search_title = request.GET.get('search_title', '')
    books_item = Books.objects.filter(title__icontains=search_title)
    return HttpResponse(serializers.serialize('json', books_item))

def show_json_by_id(request, id):
    data = Books.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def borrow_book_flutter(request, id):
    if request.method == 'POST':
        book = Books.objects.get(pk=id)
        if book.borrowed_by:
            return JsonResponse({'status': 'error', 'message': 'Someone has borrowed the book'}, status=404)
        # Retrieve user information from the POST request and update the book
        book.borrowed_by = request.user
        book.borrowed_date = date.today()  # Save the current date as borrowed_date
        book.is_borrowed = "Borrowed"
        book.amount = book.amount-1
        book.save()
        return JsonResponse({'status': 'success', 'message': 'Book borrowed successfully'})

@csrf_exempt
def borrow_book(request, id):
    if request.method == 'POST':
        book = Books.objects.get(pk=id)
        if book.borrowed_by:
            return JsonResponse({'status': 'error', 'message': 'Someone has borrowed the book'}, status=404)
        # Retrieve user information from the POST request and update the book
        book.borrowed_by = request.user
        book.borrowed_date = date.today()  # Save the current date as borrowed_date
        book.is_borrowed = "Borrowed"
        book.amount = book.amount-1
        book.save()
        return JsonResponse({'status': 'success', 'message': 'Book borrowed successfully'})
