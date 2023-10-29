from django.shortcuts import render, get_object_or_404, redirect
from user_profile_page.models import Member
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from landingPage.models import Books
from user_profile_page.models import Member
from wishlist_page.models import WishlistItem
from django.core import serializers
from landingPage.models import Books
import json
from .forms import MemberForm



@login_required
# Create your views here.
def user_dashboard(request):
    # Get the logged-in user and their bio
    user_info = request.user
    member, created = Member.objects.get_or_create(user=user_info)
    user_bio = member.bio
    borrowed_books = Books.objects.filter(borrowed_by=user_info)
    wishlisted_books = WishlistItem.objects.filter(user=user_info)
    form = MemberForm(instance=member)
    
    context = {
        'user_info': user_info,
        'user_bio': user_bio,
        'borrowed_books': borrowed_books,
        'wishlisted_books': wishlisted_books,
        'form': form
    }

    return render(request, 'main_dashboard.html', context)

def load_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        wishlist_data = [{'title': item.title} for item in wishlist_items]
        return JsonResponse({'wishlist': wishlist_data})
    else:
        return JsonResponse({'wishlist': []})
    

def load_borrowed_book(request):
    if request.user.is_authenticated:
        books_items = Books.objects.filter(borrowed_by=request.user)
        books_data = [{'title': item.title} for item in books_items]
        return JsonResponse({'books': books_data})
    else:
        return JsonResponse({'books': []})
    
def borrowed_book_check_render(request):
    user_info = request.user
    member, created = Member.objects.get_or_create(user=user_info)
    user_bio = member.bio
    borrowed_books = Books.objects.filter(borrowed_by=user_info)
    wishlisted_books = WishlistItem.objects.filter(user=user_info)
    
    context = {
        'user_info': user_info,
        'user_bio': user_bio,
        'borrowed_books': borrowed_books,
        'wishlisted_books': wishlisted_books,
    }
    return render(request, 'borrowed_book_check.html', context)

def get_borrowed_books_json(request):
    if request.user.is_authenticated:
        borrowed_books = Books.objects.filter(borrowed_by=request.user)
        data = serializers.serialize('json', borrowed_books)
        struct = json.loads(data)
        return JsonResponse(struct, safe=False)
    
def get_wishlisted_books_json(request):
    if request.user.is_authenticated:
        wishlisted_books = WishlistItem.objects.filter(user=request.user)
        data = serializers.serialize('json', wishlisted_books)
        struct = json.loads(data)
        return JsonResponse(struct, safe=False)
    
def delete_all_books(request):
    books = Books.objects.all()
    books.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
def update_bio_ajax(request):
    if request.method == 'POST':
        user = request.user
        member, created = Member.objects.get_or_create(user=user)
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            return HttpResponse(form.instance.bio, status=201)
    return HttpResponseNotFound()



@csrf_exempt
def return_book(request, id):
    if request.method == 'POST':
        book = Books.objects.get(pk=id)
        book.borrowed_by = None
        book.borrowed_date = None  # Reset the borrowed_date
        book.return_date = None  # Reset the return_date
        book.save()
        return JsonResponse({'status': 'success', 'message': 'Book borrowed successfully', 'is_borrowed': 'Borrowed'})


