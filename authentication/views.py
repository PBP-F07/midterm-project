from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from landingPage.models import Books
from landingPage.views import fetch_static_books
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            #Setting default role
            default_group = Group.objects.get(name='member')
            user.groups.add(default_group)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):

    if (len(Books.objects.all()) == 0):
        fetch_static_books()


    superuser_exists = User.objects.filter(is_superuser=True).exists()
    group_names =["member","admin"]

    for group_name in group_names:
        if not Group.objects.filter(name=group_name).exists():
            group = Group(name=group_name)
            group.save()
    
    if not superuser_exists:
        username = "PBPF07"
        email = "zaim.aydin@ui.ac.id"
        password = "pbpkelompokf07"
        User.objects.create_superuser(username, email, password)


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # menentukan role member atau admin
            if(user.groups.all()[0].name == 'admin'):
                # menuju ke admin page
                return HttpResponseRedirect(reverse('admin_page:show_main'))
            elif(user.groups.all()[0].name == 'member'):
                # menuju ke landing page
                return HttpResponseRedirect(reverse('landingPage:show_main'))
        else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

@csrf_exempt
def make_admin(request):
    username = ["adminZaim", "adminVincent", "adminDien", "adminEvan", "adminJulian"]
    password_new = "pbpkelompokf07"
    
    for new_username in username:
        new_admin = User.objects.create_user(new_username, password=password_new)
        default_group = Group.objects.get(name='admin')
        new_admin.groups.add(default_group)