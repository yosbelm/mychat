from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:id>', views.user_details, name='user_details'),
    path('chat/<int:id>', views.chatting, name='chatting'),
    path('actualchat/<int:id>/<int:r_id>', views.chat_screen, name='actualchat'),
    path('sent_msg/<int:id>/<int:r_id>', views.sentMessages, name='sent_msg'),
]