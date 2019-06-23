from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^create/profile$', views.new_user, name='new-user'),
    url(r'^my/profile$', views.new_user, name='profile'),
    
]