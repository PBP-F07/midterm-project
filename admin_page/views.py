from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

@login_required(login_url='')
def show_main(request):
    user_role = request.user.groups.all()[0].name
    print(user_role + "login")

    return HttpResponse("Ini halaman admin literaphile")
