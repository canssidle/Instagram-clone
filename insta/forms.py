from .models import Profile,Post
from django import forms

class NewUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['email']
class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['place']
    