from django.urls import path
from .views import books_details,create_comment,get_comments,delete_comment, get_replies, replies, create_reply,delete_reply,donate,delete_book_all,edit_comment,edit_reply
from .views import discussion_show_json, discussion_json, reply_show_json, reply_json, create_discussion_flutter, create_reply_flutter, edit_discussion_flutter,edit_reply_flutter
app_name = 'book_details'

urlpatterns = [
    path('<int:id>', books_details, name='books_details'),
    path('create-comment/<int:id>', create_comment, name="create_comment"),
    path('get-comments/<int:id>', get_comments, name="get_comments"),
    path('delete-comment/<int:book_id>/<int:id>', delete_comment, name='delete_comment'),
    
    path('comments/<int:id>',replies, name="replies" ),
    path('comments/get-replies/<int:id>',get_replies, name="get_replies" ),
    path('comments/create-reply/<int:id>', create_reply, name="create-reply"),
    path('comments/delete-reply/<int:comment_id>/<int:id>', delete_reply, name='delete_reply'),
    path('donate/<int:book_id>', donate , name='donate'),
    path('delete-book-all/', delete_book_all , name = 'delete_book_all'),

    path('edit-comment/<int:book_id>/<int:comment_id>', edit_comment, name='edit_comment'),
    path('comments/edit-reply/<int:comment_id>/<int:reply_id>', edit_reply, name='edit_reply'),

    path('discussions/json', discussion_show_json, name='discussion_show_json'),
    path('discussion/<int:id>/json/', discussion_json, name="discussion_json" ),
    path('replies/json', reply_show_json, name='replies_show_json'),
    path('replies/<int:id>/json/', reply_json, name="reply_json" ),
    path('create-discussion-flutter/<int:id>', create_discussion_flutter, name='create_discussion_flutter'),
    path('create-reply-flutter/<int:id>', create_reply_flutter, name='create_reply_flutter'),
    path('edit-discussion-flutter/<int:id>', edit_discussion_flutter, name='edit_discussion_flutter'),
    path('edit-reply-flutter/<int:id>', edit_reply_flutter, name='edit_reply_flutter'),
]