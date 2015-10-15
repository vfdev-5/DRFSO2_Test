from django.conf.urls import include, url

from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth import views, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest
# from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# ------- Views -------
def index(request, template_name='index.html'):
    context = {}
    return render(request, template_name, context)


def register(request, template_name='register.html'):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, template_name, context)


def auth_register(request):
    if request.method == 'POST':
        data = request.POST
        username=data.get('username', None)
        password=data.get('password', None)
        user = User.objects.create_user(username, password=password)
        return HttpResponse("OK")

    return HttpResponse("NOK")

def logout(request):
    auth_logout(request)
    return redirect("/")

# Empty url on which is redirected web-browser after requesting auth/login/<backend>
def profile(request):
    return HttpResponse()



# ------- Urls -------

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^auth/register/', auth_register),

    url(r'profile/$', profile, name='profile'),

    url(r'^$', index, name="index"),

    url(r'^register/$', register, name="register"),

    url(r'logout/$', logout, name='logout'),

    url(r'^accounts/login/$', views.login, {'template_name': 'login.html'}, name='login'),


]
