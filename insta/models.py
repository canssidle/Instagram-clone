from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Profile(models.Model):
    image = models.ImageField(upload_to='profile/', blank=True)
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    bio = models.CharField(max_length=100)
    email = models.CharField(max_length=140)

class InstaLetterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    
class Post(models.Model):
    image = models.ImageField(upload_to='feed/', blank=True)
    image_name =models.CharField(max_length=100)
    caption=models.CharField(max_length=100)
    comments=models.CharField(max_length=100)
    profile=models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.ImageField(max_length=100)
    place=models.ImageField(max_length=50)
    
   





    