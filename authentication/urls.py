from django.urls import path
from authentication.views import register, login_user, logout_user, make_admin

app_name = 'authentication'

urlpatterns = [
    path('', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('make-admin/', make_admin, name='make_admin')

]