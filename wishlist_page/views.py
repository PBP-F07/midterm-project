import hashlib
import requests
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import WishlistItem

@login_required
# fungsi untuk pencarian buku yang menggunakan google api
def search_books(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        GOOGLE_BOOKS_API_KEY = os.environ.get('GOOGLE_BOOKS_API_KEY')
        api_url = f'https://www.googleapis.com/books/v1/volumes?q={search_query}&key={GOOGLE_BOOKS_API_KEY}&maxResults=40'
        response = requests.get(api_url)
        data = response.json()
        book_data = []

        if 'items' in data:
            user_wishlist = WishlistItem.objects.filter(user=request.user).values_list('title', flat=True)

            for item in data['items']:
                title = item['volumeInfo']['title']
                # validasi bahwa buku belum ada di user wishlist
                if title not in user_wishlist:
                    book_info = {
                        'title': title,
                        'author': ', '.join(item['volumeInfo']['authors']) if 'authors' in item['volumeInfo'] else 'Unknown Author',
                        'description': item['volumeInfo']['description'] if 'description' in item['volumeInfo'] else '',
                        'image': item['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in item['volumeInfo'] else '',
                        'year_of_release': item['volumeInfo']['publishedDate'][:4] if 'publishedDate' in item['volumeInfo'] else '',
                    }
                    book_data.append(book_info)
        return render(request, 'main_wishlist.html', {'book_data': book_data, 'user_wishlist': user_wishlist})
    return render(request, 'main_wishlist.html', {'book_data': []})

# fungsi untuk menambahkan buku ke wishlist
def add_to_wishlist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        image = request.POST.get('image')
        year_of_release = request.POST.get('year_of_release')

        WishlistItem.objects.create(
            user=request.user,
            title=title,
            author=author,
            description=description,
            image=image,
            year_of_release=year_of_release
        )

        return JsonResponse({'message': 'Added to wishlist'})
    return JsonResponse({'message': 'Invalid request method'}, status=400)

# fungsi untuk menampilkan data wishlist user
def load_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        wishlist_data = [{'title': item.title} for item in wishlist_items]
        return JsonResponse({'wishlist': wishlist_data})
    else:
        return JsonResponse({'wishlist': []})
