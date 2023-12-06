from django.urls import path
from authentication.views import register, login_user, logout_user, make_admin, login_mobile, register_mobile, logout_mobile

app_name = 'authentication'

urlpatterns = [
    path('', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('make-admin/', make_admin, name='make_admin'),
    path('login/', login_mobile, name='login_mobile'),
    path('register-mobile/', register_mobile, name="register_mobile"),
    path('logout-mobile/', logout_mobile, name="logout_mobile")
]