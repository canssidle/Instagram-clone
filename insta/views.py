from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from .email import send_welcome_email
from django.http import HttpResponse, Http404,HttpResponseRedirect,request


# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    image_form = PostForm()
    image = Post.objects.all()
    commentform = CommentForm()
    return render(request,'home.html')

def new_user(request):
    current_user = request.user
    if request.method == 'POST':
        name = form.cleaned_data['your_name']
        email = form.cleaned_data['email']
        recipient = InstaLetterRecipients(name = name,email =email)
        form = NewUserForm(request.POST, request.FILES)
        recipient.save()
        send_welcome_email(name,email)


        if form.is_valid():
            article = form.save(commit=False)
            
            article.save()
            # return redirect(new_user)
            
 
    else:
        form = NewUserForm()
    return render(request, 'new_user.html', {"form": form,"letterForm":form})

    
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.save()
      

    else:
        form = NewPostForm()
    return render(request, 'new_article.html', {"form": form})


    return render(request,'profile.html')


