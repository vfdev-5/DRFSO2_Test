# Django
from django.conf.urls import include, url
from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth import views, logout as auth_logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.http import HttpResponse, HttpRequest
# from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# DRF
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from local_tokens import get_or_create_token, get_or_create_token2

# ------- Views -------
def index(request, template_name='index.html'):

    user = request.user
    access_token=None
    provider=None
    expires=None
    if user.is_authenticated():
        # get the last login provider
        try:
            provider = request.session['social_auth_last_login_backend']
            social = user.social_auth.get(provider=provider)
            access_token = social.extra_data['access_token']
            expires = social.extra_data['expires']
        except KeyError:
            print "This is an ordinary user without social network backend"
            # Issue an access_token
            token = get_or_create_token(user)
            if token is not None:
                access_token = token.token
                provider = None
                expires = token.expires

        if not access_token:
            auth_logout(request)

    context = {
        "access_token": access_token,
        "provider": provider,
        "expires": expires,
    }
    return render(request, template_name, context)


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", )

def register(request, template_name='register.html'):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, template_name, context)


def logout(request):
    auth_logout(request)
    return redirect("/")

# Empty url on which is redirected web-browser after requesting auth/login/<backend>
def profile(request):
    return HttpResponse()


# Protected api resource
@api_view(['GET'])
def api_protected(request):

    # user = request.user.backend.do_auth(request.auth)
    # print user

    # return Response({"message": user.username + ", welcome to the API!"})
    return Response({"message": "This is a protected message."})

# Open api resource
@api_view(['GET'])
@permission_classes((AllowAny, ))
def api_open(request):
    return Response({"message": "Welcome to the open ressource."})


# Open api resource
@api_view(['POST'])
@permission_classes((AllowAny, ))
def api_register(request):

    params = request.POST
    print "POST : ", params
    username = params.get('username', None)
    email = params.get('email', None)
    password = params.get('password', None)
    if username and password and email:
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username, email=email, password=password)
            return Response({"message": "User " + user.username + " is registered"})
        else:
            return Response({"error": "User already exists"})

    return Response({"error": "User is not registered!"})





# ------- Urls -------

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),

    url(r'^auth/', include('rest_framework_social_oauth2.urls')),

    url(r'profile/$', profile, name='profile'),

    url(r'^$', index, name="index"),

    url(r'^register/$', register, name="register"),

    url(r'logout/$', logout, name='logout'),

    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^api/$', api_open, name="api"),
    url(r'^api/protected/$', api_protected, name="protected"),
    url(r'^api/register/$', api_register, name="api_register")


]
