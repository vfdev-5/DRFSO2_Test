from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth import views, logout as auth_logout
from django.http import HttpResponse

# ------- Views -------
def index(request, template_name='index.html'):
    context = {}
    return render(request, template_name, context)

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

    url(r'profile/$', profile, name='profile'),

    url(r'^$', index, name="index"),


    url(r'logout/$', logout, name='logout'),

    url(r'^accounts/login/$', views.login, {'template_name': 'login.html'}, name='login'),


]
