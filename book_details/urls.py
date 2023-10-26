from django.urls import path
from .views import books_details,create_comment,get_comments

app_name = 'book_details'

urlpatterns = [
    path('<int:id>', books_details, name='book_details'),
    path('create-comment/<int:id>', create_comment, name="create_comment"),
    path('get-comments/<int:id>', get_comments, name="get_comments"),
]