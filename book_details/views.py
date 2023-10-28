from django.shortcuts import render
from landingPage.models import Books
from django.views.decorators.csrf import csrf_exempt
from .models import discussion, reply
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
import datetime


def books_details(request,id):
    user = request.user.username
    book = Books.objects.filter(pk=id)[0]
    date = datetime.datetime.now()
    format = "%H %d-%m-%Y "
    context = {
        'user' : user,
        'book' : book,
        'date' : date.strftime(format)
    }

    return render(request, "book_details_main.html", context)

def get_comments(request,id):
    comments = discussion.objects.filter(book_id=id)
    return HttpResponse(serializers.serialize('json', comments))

def delete_comment(request,book_id,id):
    comments = discussion.objects.get(pk=id)
    comments.delete()
    return HttpResponseRedirect(reverse('book_details:books_details',kwargs={"id": book_id}))
    

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


