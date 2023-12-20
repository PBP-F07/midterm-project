import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from wishlist_page.models import WishlistItem, addWishlist
from landingPage.models import Books

@login_required(login_url='')
def show_main(request):
    # user_role = request.user.groups.all()[0].name
    try:
        group = Group.objects.get(name='member')
        users_in_group = list(group.user_set.all())
    except Group.DoesNotExist:
        users_in_group = []

    # user group / role
    groups = request.user.groups.all()

    context = {
        'name': request.user.username,
        'role': groups[0].name,
        'members': users_in_group,
        'total_books': len(Books.objects.all())
    }

    return render(request, "wish_req.html", context)

def show_userpage(request):
    users = User.objects.all()
    groups = request.user.groups.all()

    context = {
        'name': request.user.username,
        'role': groups[0].name,
        'users': users
    }
    return render(request, "users.html", context)

def show_managebooks(request):
    groups = request.user.groups.all()
    context ={
        'name': request.user.username,
        'role': groups[0].name
    }

    return render(request, "managebooks.html", context)

def show_notes(request):
    notes = addWishlist.objects.all()
    groups = request.user.groups.all()

    context = {
        'name': request.user.username,
        'role': groups[0].name,
        'notes': notes
    }
    return render(request, "notes.html", context)

def show_json(request):
    wishlist = WishlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", wishlist), content_type="application/json")

def get_allbooks_json(request):
    books = Books.objects.all()
    return HttpResponse(serializers.serialize("json", books))

def get_wishlist_json(request):
    wishlist = WishlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", wishlist))

def get_allusers_mobile(request):
    users = User.objects.all()
    user_data = []
    for user in users:
        user_data.append({
            'id': user.pk,
            'username': user.username,
            'role': user.groups.first().name if user.groups.exists() else None,
        })
    response_data = {
        'users': user_data
    }

    return JsonResponse(response_data, safe=False)

def get_wishlist_mobile(request):
    wishlist = WishlistItem.objects.all()
    wishlist_json = serializers.serialize('json', wishlist)
    return JsonResponse({'wishlist': wishlist_json}, safe=False)

def get_allbooks_mobile(request):
    books = Books.objects.all()
    books_json = serializers.serialize('json', books)
    return JsonResponse({'books': books_json}, safe=False)

@csrf_exempt
@require_http_methods(['DELETE'])
def reject_wishlist(request, id):
    book = WishlistItem.objects.filter(id=id)
    book.delete()
    return HttpResponse(b"REJECTED", status=200)

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_book(request, id):
    book = Books.objects.filter(id=id)
    book.delete()
    return HttpResponse(b"DELETED", status=200)

@csrf_exempt
@require_http_methods(['POST'])
def add_catalog(request, id):
    # json_file_path = 'static/admin/books_data.json'
    requested_book = WishlistItem.objects.filter(id=id)[0]

    title = requested_book.title
    authors = requested_book.author
    description = requested_book.description
    cover_img = requested_book.image
    release_year = requested_book.year_of_release
    amount = 10

    new_book = Books(title=title, author=authors, description=description, image=cover_img, year_of_release=release_year, amount=amount)
    new_book.save()

    return HttpResponse(b"CREATED", status=201)

@require_http_methods(['GET'])
def get_book_by_title(request):
    title = request.GET.get('title', '')
    books = Books.objects.filter(title__icontains=title)

    book_data = []
    for book in books:
        book_data.append({
            'id': book.pk,
            'title': book.title,
            'author': book.author,
            'year_of_release': book.year_of_release,
        })

    return JsonResponse(book_data, safe=False)

@require_http_methods(['GET'])
def get_book_by_title_mobile(request):
    title = request.GET.get('title', '')
    books = Books.objects.filter(title__icontains=title)

    search_json = serializers.serialize('json', books)
    return JsonResponse({'books': search_json}, safe=False) 