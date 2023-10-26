from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from wishlist_page import models

@login_required(login_url='')
def show_main(request):
    user_role = request.user.groups.all()[0].name

    context = {
        'name': request.user.username
    }

    return render(request, "admin.html", context)

