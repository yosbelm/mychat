from django.shortcuts import render, redirect
from .models import Profile, ChatMessage
from .forms import MessageForm
from django.http import JsonResponse
import json

# Create your views here.
def user_details(request, id):
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
    user_receiver = Profile.objects.get(id = r_id)
    chat_send = ChatMessage.objects.filter(sender_id = id, receiver_id = r_id)
    chat_receive = ChatMessage.objects.filter(sender_id = r_id, receiver_id = id)
    mensaje_sent = []
    mensaje_received = []
    
    for message in chat_send:
        if message.sender.id==user.id and message.receiver.id==user_receiver.id:
            mensaje_sent.append(message.body)
            
            print(message.sender.id, message.receiver.id, mensaje_sent)
            
    print('*******************************************')
    for message in chat_receive:
        if message.receiver.id==user.id and message.sender.id==user_receiver.id:
            mensaje_received.append(message.body)
            
            print(message.sender.id, message.receiver.id, mensaje_received)
                
    frnd = user.friend.all()
    friend = user.friend.get(id= r_id)

    if request.method == 'POST':
        form = ChatMessage.objects.create(body=request.POST['body'], sender=user,receiver=user_receiver, seen=False)
        return redirect('actualchat', id, r_id)
    else:
        form = MessageForm()
    context ={'user': user, 'form': form, 'frnd': frnd, 'mensaje_sent': mensaje_sent, 'mensaje_received': mensaje_received, 'chat_send': chat_send, 'chat_receive': chat_receive, 'friend':friend}
    return render(request, 'actualchat.html', context)


def sentMessages(request, id, r_id):
    user = Profile.objects.get(id=id)
    user_receiver = Profile.objects.get(id = r_id)
    
    data = json.loads(request.body)
    new_chat = data['msg']
    final_msg = ChatMessage.objects.create(body=new_chat, sender=user,receiver=user_receiver, seen=False)
    
    respuesta = {'mensaje': final_msg.body, 'usuario_id': id, 'receptor_id': r_id}
    return JsonResponse(respuesta, safe=False)
    