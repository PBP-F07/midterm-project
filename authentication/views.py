import json
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

@csrf_exempt
def login_mobile(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

            # Retrieve user's group information
            user_group = user.groups.first() if user.groups.exists() else None

            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                "group": user_group.name if user_group else None
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def register_mobile(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)

        username = data["username"]
        password1 = data["password1"]
        password2 = data["password2"]

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Gagal membuat akun'})

        new_user = User.objects.create_user(username = username, password = password1)
        new_user.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def logout_mobile(request):
    username = request.user.username

    try:
        logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)