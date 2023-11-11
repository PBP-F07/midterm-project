import requests
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import WishlistItem, addWishlist
from django.views.decorators.csrf import csrf_exempt
from landingPage.models import Books
from django.core import serializers
from wishlist_page.forms import BookForm
from wishlist_page.models import newWishlist

@login_required
# fungsi untuk pencarian buku yang menggunakan google api
def search_books(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        GOOGLE_BOOKS_API_KEY = 'AIzaSyDX3PLT7tAjUA0-ZLaSsfKVi1yS_CRp4PI'
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
                        'image': item['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in item['volumeInfo'] else 'https://s3.amazonaws.com/media.muckrack.com/profile/images/317132/loudmouthjulia.jpeg.256x256_q100_crop-smart.jpg',
                        'year_of_release': item['volumeInfo']['publishedDate'][:4] if 'publishedDate' in item['volumeInfo'] else '',
                    }
                    book_data.append(book_info)
        return render(request, 'main_wishlist.html', {'book_data': book_data, 'user_wishlist': user_wishlist})
    return render(request, 'main_wishlist.html', {'book_data': []})

# fungsi untuk menambahkan notes wishlist berupa buku yang tidak ditemukan
def create_notes(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        notes = form.save(commit=False)
        notes.user = request.user
        notes.save()
        return HttpResponseRedirect(reverse('wishlist_page:search_books'))
    
    context = {'form': form}
    return render(request, "create_notes.html", context)


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
        wishlist_data = []
        
        for item in wishlist_items:
            book_exists = Books.objects.filter(title=item.title).exists()
            status = "sudah tersedia" if book_exists else "sedang diproses"
            wishlist_data.append({'id': item.pk, 'title': item.title, 'author':item.author, 'status': status})
        
        return JsonResponse({'wishlist': wishlist_data})
    else:
        return JsonResponse({'wishlist': []})

# fungsi untuk menghapus buku dengan AJAX
@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        product = WishlistItem.objects.get(id=id, user=request.user)
        product.delete()
        return HttpResponse(b"CREATED", status=201)
    
# fungsi untuk menambah buku dengan AJAX
@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        image = request.POST.get("image")
        year_of_release = request.POST.get("year_of_release")

        new_book = WishlistItem(user=user, title=title, author=author, description=description, image=image, year_of_release=year_of_release)
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_json(request):
    data = addWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
