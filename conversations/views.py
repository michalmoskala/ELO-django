from django.shortcuts import render, get_object_or_404
from .models import Conversation
from msgs.forms import MessageForm
from msgs.models import Msg

def ConversationDetailView(request, id):
    obj = get_object_or_404(Conversation, id=id)
    new_messages = Msg.objects.filter(receiver_id=id)
    form = MessageForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()
        form = MessageForm()    
    context = {
        "object": obj,
        "new_messages": new_messages,
        "form": form
    }
    return render(request, "conversations/conversation_detail.html", context)


