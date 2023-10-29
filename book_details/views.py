from django.shortcuts import render
from landingPage.models import Books
from django.views.decorators.csrf import csrf_exempt
from .models import discussion, reply
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url='')
def books_details(request,id):
    user = request.user.username
    book = Books.objects.filter(pk=id)[0]
    date = datetime.datetime.now()
    format = "%H %d-%m-%Y "
    context = {
        'name' : user,
        'book' : book,
        
    }

    return render(request, "book_details_main.html", context)

@login_required(login_url='')
def replies(request,id):
    user = request.user.username
    comment = discussion.objects.filter(pk=id)[0]
    context = {
        'name' : user,
        'comment' : comment,
    }

    return render(request, "replies.html", context)


def get_comments(request,id):
    comments = discussion.objects.filter(book_id=id)
    return HttpResponse(serializers.serialize('json', comments))

def delete_comment(request,book_id,id):
    comments = discussion.objects.get(pk=id)
    comments.delete()
    return HttpResponseRedirect(reverse('book_details:books_details',kwargs={"id": book_id}))

def get_replies(request,id):
    replies = reply.objects.filter(comment_id=id)
    return HttpResponse(serializers.serialize('json', replies))

def delete_reply(request,comment_id,id):
    replies = reply.objects.get(pk=id)
    replies.delete()
    return HttpResponseRedirect(reverse('book_details:replies',kwargs={"id": comment_id}))

@csrf_exempt
def create_comment(requset,id):
    if requset.method == 'POST':
        user = requset.user.username
        format = "%H %d-%m-%Y "
        date = datetime.datetime.now().strftime(format)
        comment = requset.POST.get("comment")
        book = Books.objects.filter(pk=id)[0]
        new_comment = discussion(comment=comment, book=book, user=user, date_added=date)
        new_comment.save()
    
        return HttpResponse(b"CREATED",status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_reply(requset,id):
    if requset.method == 'POST':
        user = requset.user.username
        replies = requset.POST.get("reply")
        print(reply)
        format = "%H %d-%m-%Y "
        date = datetime.datetime.now().strftime(format)
        comments = discussion.objects.filter(pk=id)[0]
        new_reply = reply(comment=comments, replies=replies, user=user, date_add=date)
        new_reply.save()
    
        return HttpResponse(b"CREATED",status=201)
    return HttpResponseNotFound()


