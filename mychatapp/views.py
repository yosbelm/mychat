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
    
    friends = Profile.objects.exclude(id=id)
    
    last_msg = []
    nnm = "No messages"
    for f in friends:
        messages = ChatMessage.objects.filter(receiver=user, sender=f)
        if len(messages) == 0:
            last_msg.append({'friend_id': f.id, 'mensaje': nnm})
        else:
            ultimo = len(messages) - 1
            last_msg.append({'friend_id': f.id, 'mensaje': messages[ultimo]})
    print(last_msg)
    context = {'user': user, 'frnd': frnd, 'last_msg': last_msg}
    return render(request,  'whatsapp.html', context)


def unreadMessagesCount(request, user_id):
    user = Profile.objects.get(id=user_id)
    friends = Profile.objects.exclude(id=user_id)  # Todos menos el usuario actual
    unread_counts = []

    for friend in friends:
        count = ChatMessage.objects.filter(sender=friend, receiver=user, seen=False).count()
        unread_counts.append({'friend_id': friend.id, 'unread_count': count})

    return JsonResponse(unread_counts, safe=False)


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
            
    for message in chat_receive:
        if message.receiver.id==user.id and message.sender.id==user_receiver.id:
            mensaje_received.append(message.body)
                
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


def receiveMessages(request, id, r_id):
    user = Profile.objects.get(id=id)
    user_receiver = Profile.objects.get(id = r_id)
    
    final_msg = ChatMessage.objects.filter(sender=user_receiver, receiver=user, seen=False).order_by('id')
    recibidos = [{'id': msg.id, 'body': msg.body} for msg in final_msg]
    
    final_msg.update(seen=True)
    return JsonResponse(recibidos, safe=False)