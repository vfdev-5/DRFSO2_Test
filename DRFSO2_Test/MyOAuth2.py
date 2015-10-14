# -*- coding: utf-8 -*-

from social.backends.oauth import BaseOAuth2
from django.core.urlresolvers import reverse

class MyOAuth2(BaseOAuth2):
    """Default OAuth2 authentication backend used by this package"""
    name = "MyOAuth2"
    # AUTHORIZATION_URL = reverse('authorize')
    AUTHORIZATION_URL = 'http://127.0.0.1:8000/auth/authorize/'
    #ACCESS_TOKEN_URL = reverse('token')
    ACCESS_TOKEN_URL = 'http://127.0.0.1:8000/auth/token/'
    ACCESS_TOKEN_METHOD = 'POST'