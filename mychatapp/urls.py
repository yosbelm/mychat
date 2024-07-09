from django.urls import path
from . import views

urlpatterns = [
    path('auth/register?username=<str:user>&password=t<str:password>', views.authentication, name='authentication'),
    path('user/<int:id>', views.user_details, name='user_details'),
    path('chat/<int:id>', views.chatting, name='chatting'),
    path('actualchat/<int:id>/<int:r_id>', views.chat_screen, name='actualchat'),
    path('sent_msg/<int:id>/<int:r_id>', views.sentMessages, name='sent_msg'),
    path('received_msg/<int:id>/<int:r_id>', views.receiveMessages, name='received_msg'),
    path('unread_messages_count/<int:user_id>/', views.unreadMessagesCount, name='unread_messages_count'),
]