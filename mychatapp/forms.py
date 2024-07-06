from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"form", "rows": 2,"placeholder": 'Type your message'}))
    class Meta:
        model = ChatMessage
        fields = ['body', ]