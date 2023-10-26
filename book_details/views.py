from django.shortcuts import render
from landingPage.models import Books
from django.views.decorators.csrf import csrf_exempt
from .models import discussion, reply
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers


def books_details(request,id):
    user = request.user.username
    book = Books.objects.filter(pk=id)[0]
    context = {
        'user' : user,
        'book' : book,
    }

    return render(request, "book_details.html", context)

def get_comments(request,id):
    comments = discussion.objects.filter(book_id=id)
    return HttpResponse(serializers.serialize('json', comments))

@csrf_exempt
def create_comment(requset,id):
    if requset.method == 'POST':
        user = requset.user.username
        comment = requset.POST.get("comment")
        book = Books.objects.filter(pk=id)[0]
        new_comment = discussion(comment=comment, book=book, user=user)
        new_comment.save()
    
        return HttpResponse(b"CREATED",status=201)
    return HttpResponseNotFound()


