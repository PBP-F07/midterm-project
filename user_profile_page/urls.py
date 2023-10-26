from django.urls import path
from . import views

app_name = 'user_profile_page'

urlpatterns = [
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('update-bio-ajax/', views.update_bio_ajax, name='update_bio_ajax'),
]