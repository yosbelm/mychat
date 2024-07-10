from django import forms
from django.forms import ModelForm
from .models import ChatMessage, Profile

class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"form", "rows": 2,"placeholder": 'Type your message'}))
    class Meta:
        model = ChatMessage
        fields = ['body', ]
        
class AuthForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)

    
    