from django.shortcuts import render
from .models import Profile, ChatMessage
from .forms import MessageForm

# Create your views here.
def index(request, id):
    user = Profile.objects.get(id=id)
    context = {'user': user}
    return render(request,  'index.html', context)

def chatting(request, id):
    user = Profile.objects.get(id=id)
    frnd = user.friend.all()
    # f = frnd.
    # print(f)
    context = {'user': user, 'frnd': frnd}
    return render(request,  'whatsapp.html', context)

def chat_screen(request, id, r_id):
    user = Profile.objects.get(id=id)
    chat_send = ChatMessage.objects.get(sender_id = id)
    chat_receive = ChatMessage.objects.get(sender_id = r_id)
    frnd = user.friend.all()
    form = MessageForm()
    context ={'user': user, 'form': form, 'frnd': frnd, 'chat_send': chat_send, 'chat_receive': chat_receive}
    return render(request, 'actualchat.html', context)
