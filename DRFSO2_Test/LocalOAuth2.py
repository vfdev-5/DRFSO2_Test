# -*- coding: utf-8 -*-
# from django.http import HttpRequest
# from requests import HTTPError
from django.core.urlresolvers import reverse

from social.backends.oauth import BaseOAuth2

from .settings import LOCALOAUTH2_API_URL

class LocalOAuth2(BaseOAuth2):

    """My OAuth2 authentication backend used by this package"""
    name = "LocalOAuth2"

    AUTHORIZATION_URL = LOCALOAUTH2_API_URL + reverse('authorize')
    # AUTHORIZATION_URL = 'http://127.0.0.1:8000/auth/authorize/'
    # AUTHORIZATION_URL = HttpRequest.build_absolute_uri('authorize')
    ACCESS_TOKEN_URL = LOCALOAUTH2_API_URL + reverse('token')
    # ACCESS_TOKEN_URL = 'http://127.0.0.1:8000/auth/token/'
    # ACCESS_TOKEN_URL = HttpRequest.build_absolute_uri('token')
    REVOKE_TOKEN_URL = LOCALOAUTH2_API_URL + reverse('revoke_token')
    ACCESS_TOKEN_METHOD = 'POST'
    API_URL = LOCALOAUTH2_API_URL

    print "ACCESS_TOKEN_URL:", ACCESS_TOKEN_URL
    print "AUTHORIZATION_URL:", AUTHORIZATION_URL
    print "REVOKE_TOKEN_URL:", REVOKE_TOKEN_URL
    print "API_URL:", API_URL

    def api_url(self):
        return self.API_URL

    def get_user_details(self, response, *args, **kwargs):
        """Return user details"""
        first_name = response.get('first_name') or ''
        last_name = response.get('last_name') or ''
        return {'username': response.get('username'),
                'email': response.get('email') or '',
                'fullname': first_name + " " + last_name,
                'first_name': first_name,
                'last_name': last_name}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        user = kwargs.get('user', None)
        data = {}
        if user:
            data['email'] = user.email
            data['username'] = user.username
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['groups'] = user.groups
            data['date_joined'] = user.date_joined

        return data

