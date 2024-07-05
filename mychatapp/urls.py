from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:id>', views.index, name='user'),
    path('chat/<int:id>', views.chatting, name='chatting'),
    path('actualchat/<int:id>/<int:r_id>', views.chat_screen, name='actualchat')
]