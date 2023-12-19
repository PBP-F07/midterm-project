from django.shortcuts import render
from landingPage.models import Books
from django.views.decorators.csrf import csrf_exempt
from .models import discussion, reply
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from .forms import CommentForm,ReplyForm
import json
from django.http import JsonResponse

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

def delete_book_all(request):
    book = Books.objects.all()
    book.delete()
    return HttpResponse(b"DELETED",status=201)

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
        format = "%H %d-%m-%Y "
        date = datetime.datetime.now().strftime(format)
        comments = discussion.objects.filter(pk=id)[0]
        new_reply = reply(comment=comments, replies=replies, user=user, date_add=date)
        new_reply.save()
    
        return HttpResponse(b"CREATED",status=201)
    return HttpResponseNotFound()

def donate(request,book_id):
    book = Books.objects.get(pk=book_id)
    book.amount = book.amount+1
    book.save()
    return HttpResponseRedirect(reverse('book_details:books_details',kwargs={"id": book_id}))

def edit_comment(request, book_id, comment_id):

    comment = discussion.objects.get(pk=comment_id)

    form = CommentForm(request.POST or None, instance=comment)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('book_details:books_details',kwargs={"id": book_id}))
    
    context = {'form': form}
    return render(request, "edit_comment.html", context)

def edit_reply(request, comment_id, reply_id):

    replies = reply.objects.get(pk=reply_id)

    form = ReplyForm(request.POST or None, instance=replies)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('book_details:replies',kwargs={"id": comment_id}))
    
    context = {'form': form}
    return render(request, "edit_reply.html", context)


#Fungsi dibawah ini untuk kepentingan flutter
@csrf_exempt
def discussion_show_json(request):
    data = discussion.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def discussion_json(request,id):
    book = discussion.objects.filter(book_id=id)
    return HttpResponse(serializers.serialize("json", book), content_type="application/json")

@csrf_exempt
def reply_show_json(request):
    comments = reply.objects.all()
    return HttpResponse(serializers.serialize("json", comments), content_type="application/json")

def reply_json(request,id):
    replies = reply.objects.filter(comment_id=id)
    return HttpResponse(serializers.serialize("json", replies), content_type="application/json")

@csrf_exempt
def create_discussion_flutter(request,id):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        format = "%H %d-%m-%Y "

        new_discussion = discussion.objects.create(
            user = request.user.username,
            comment = data["discussion"],
            date_added = datetime.datetime.now().strftime(format),
            book = Books.objects.filter(pk=id)[0]
        )

        new_discussion.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    

@csrf_exempt
def create_reply_flutter(request,id):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        format = "%H %d-%m-%Y "

        new_reply = reply.objects.create(
            user = request.user.username,
            comment = discussion.objects.filter(pk=id)[0],
            date_add = datetime.datetime.now().strftime(format),
            replies = data["replies"],
        )

        new_reply.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

