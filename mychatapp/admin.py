from django.contrib import admin
from .models import Profile, Friends, ChatMessage

# Register your models here.
admin.site.register([Friends, Profile, ChatMessage])