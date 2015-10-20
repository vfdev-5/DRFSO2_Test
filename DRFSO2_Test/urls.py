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

# Oauth2 provider
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.oauth2_backends import OAuthLibCore
from oauthlib.common import Request

# ------- Views -------
def index(request, template_name='index.html'):

    user = request.user
    access_token=None
    provider=None
    expires=None
    if user.is_authenticated:
        # get the last login provider
        try:
            provider = request.session['social_auth_last_login_backend']
            social = user.social_auth.get(provider=provider)
            access_token = social.extra_data['access_token']
            expires = social.extra_data['expires']
        except KeyError:
            print "This is an ordinary user without social network backend"
            # Issue an access_token
            # TokenEndpoint.create_token_response from /home/vfdev/Documents/WebDev/venv/lib/python2.7/site-packages/oauthlib/oauth2/rfc6749/endpoints/token.py
            # /home/vfdev/Documents/WebDev/venv/lib/python2.7/site-packages/oauthlib/oauth2/rfc6749/grant_types/resource_owner_password_credentials.py
            #         token = token_handler.create_token(request, self.refresh_token)
            #
            # uri : u'/auth/token/'
            # http_method : 'POST'
            # body : u'username=userthree&client_secret=C5tdn1Q0NW95sd8MmJFm64SObyjGUv1pnXmCHebJ1hSkWHKXQqR3OhJTLHPAoMJVaKpfRM59iy29z7WpIQsZyGrH670FgZ9R5FeHzKU4tyuAvmq9t5IpNn6zGEZlwSzW&password=345&grant_type=password&client_id=KSo05DIhGLGiKcJuraW0hvORl68WyfhBUhrjkZoE'
            #
            # headers = {'RUN_MAIN': 'true', 'SERVER_SOFTWARE': 'WSGIServer/0.1 Python/2.7.9', 'SCRIPT_NAME': u'', 'REQUEST_METHOD': 'POST', 'SERVER_PROTOCOL': 'HTTP/1.1', 'HOME': '/home/vfdev', 'LD_LIBRARY_PATH': '/home/vfdev/pycharm-community-4.5.3/bin:', 'XDG_SESSION_DESKTOP': 'xfce', 'SHELL': '/bin/bash', 'XDG_DATA_DIRS': '/usr/share/xfce4:/usr/local/share/:/usr/share/:/usr/share', 'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-fxcFMwoxx7,guid=88c8c64c8c411618f8bdcf46561cf7b8', 'SERVER_PORT': '8000', 'USERNAME': 'vfdev', 'XDG_RUNTIME_DIR': '/run/user/1000', 'PYTHONPATH': '/home/vfdev/Documents/WebDev/DRFSO2_Test', 'HTTP_HOST': '127.0.0.1:8000', 'XDG_SESSION_ID': '1', 'IDE_PROJECT_ROOTS': '/home/vfdev/Documents/WebDev/DRFSO2_Test', 'HTTP_ACCEPT': '*/*', 'DESKTOP_SESSION': 'xfce', 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.multiprocess': False, 'PYCHARM_HOSTED': '1', 'XDG_MENU_PREFIX': 'xfce-', 'PATH_INFO': u'/auth/token/', 'PYTHONIOENCODING': 'UTF-8', 'GLADE_PIXMAP_PATH': ':', 'XDG_CURRENT_DESKTOP': 'XFCE', 'XDG_VTNR': '7', 'LOGNAME': 'vfdev', 'USER': 'vfdev', 'QUERY_STRING': '', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/home/vfdev/Documents/WebDev/venv/bin', 'PYTHONUNBUFFERED': '1', 'SSH_AGENT_PID': '1612', 'TERM': 'emacs', 'HTTP_USER_AGENT': 'curl/7.38.0', 'TZ': 'UTC', 'XAUTHORITY': '/var/run/gdm3/auth-for-vfdev-TXwS5x/database', 'SERVER_NAME': 'localhost', 'SESSION_MANAGER': 'local/debian:@/tmp/.ICE-unix/1626,unix/debian:/tmp/.ICE-unix/1626', 'DISPLAY': ':0.0', 'wsgi.url_scheme': 'http', 'WINDOWPATH': '7', 'GLADE_CATALOG_PATH': ':', 'GPG_AGENT_INFO': '/tmp/gpg-TkstFx/S.gpg-agent:1633:1', 'CONTENT_LENGTH': '245', 'GLADE_MODULE_PATH': ':', 'SSH_AUTH_SOCK': '/tmp/ssh-iqjoF3R2JaoR/agent.1534', 'GDMSESSION': 'xfce', 'wsgi.multithread': True, 'XDG_SEAT': 'seat0', 'LANG': 'en_US.UTF-8', 'XDG_CONFIG_DIRS': '/etc/xdg', 'GATEWAY_INTERFACE': 'CGI/1.1', 'REMOTE_HOST': '', 'REMOTE_ADDR': '127.0.0.1', 'PWD': '/home/vfdev', 'DJANGO_SETTINGS_MODULE': 'DRFSO2_Test.settings', 'CONTENT_TYPE': 'application/x-www-form-urlencoded', 'wsgi.file_wrapper': <class wsgiref.util.FileWrapper at 0x7f451b6b7390>, u'CSRF_COOKIE': u'UznyNyLGiMHELaPd8Ex7U5VQe58ortQ4'}
            #
            #
            # from /home/vfdev/Documents/WebDev/venv/lib/python2.7/site-packages/oauth2_provider/oauth2_backends.py
            #
            #     def extract_headers(self, request):
            #         """
            #         Extracts headers from the Django request object
            #         :param request: The current django.http.HttpRequest object
            #         :return: a dictionary with OAuthLib needed headers
            #         """
            #         headers = request.META.copy()
            #         if 'wsgi.input' in headers:
            #             del headers['wsgi.input']
            #         if 'wsgi.errors' in headers:
            #             del headers['wsgi.errors']
            #         if 'HTTP_AUTHORIZATION' in headers:
            #             headers['Authorization'] = headers['HTTP_AUTHORIZATION']
            #
            #         return headers
            #
            #
            # uri = u'/auth/token/'
            # body = None
            # headers = None
            # token_request = Request(uri, http_method='POST', body=body, headers=headers)
            #
            # oauth_core = OAuthLibMixin.get_oauthlib_core()
            # server = oauth_core.server
            # token_handler = server.default_token_type
            # access_token = token_handler.create_token(token_request)
            # provider = "Local"
            pass

        if not access_token or not provider:
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
