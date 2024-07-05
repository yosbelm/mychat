from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='media', blank=True, null= True)
    about = models.CharField(max_length=200, blank=True, null= True)
    friend = models.ManyToManyField('self', blank=True)
    
    
    def __str__(self):
        return self.name

class Friends(models.Model):
    frnd_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.frnd_profile.name
    
    
class ChatMessage(models.Model):
    body = models.CharField(max_length=500)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body