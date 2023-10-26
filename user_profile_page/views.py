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


@login_required
# Create your views here.
def user_dashboard(request):
    # Get the logged-in user and their bio
    user_info = request.user
    member, created = Member.objects.get_or_create(user=user_info)
    user_bio = member.bio
    borrowed_books = Books.objects.filter(borrowed_by=user_info)
    
    context = {
        'user_info': user_info,
        'user_bio': user_bio,
        'borrowed_books': borrowed_books,
    }

    return render(request, 'main_dashboard.html', context)

def load_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        wishlist_data = [{'title': item.title} for item in wishlist_items]
        return JsonResponse({'wishlist': wishlist_data})
    else:
        return JsonResponse({'wishlist': []})

@csrf_exempt
def update_bio_ajax(request):
    if request.method == 'POST':
        bio = request.POST.get("bio")
        user = request.user

        # Update the bio in the Member model
        member, created = Member.objects.get_or_create(user=user)
        member.bio = bio
        member.save()

        return HttpResponse(member.bio, status=201)
    
    return HttpResponseNotFound()
