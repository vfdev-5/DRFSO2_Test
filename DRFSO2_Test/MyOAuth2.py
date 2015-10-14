# -*- coding: utf-8 -*-

from social.backends.oauth import BaseOAuth2
from django.core.urlresolvers import reverse
from requests import HTTPError
# from six.moves.urllib.parse import urljoin

class MyOAuth2(BaseOAuth2):

    """My OAuth2 authentication backend used by this package"""
    name = "MyOAuth2"
    # AUTHORIZATION_URL = reverse('authorize')
    AUTHORIZATION_URL = 'http://127.0.0.1:8000/auth/authorize/'
    #ACCESS_TOKEN_URL = reverse('token')
    ACCESS_TOKEN_URL = 'http://127.0.0.1:8000/auth/token/'
    ACCESS_TOKEN_METHOD = 'POST'

    API_URL = 'https://api.github.com/'

    def api_url(self):
        return self.API_URL

    def get_user_details(self, response):
        """Return user details from local DB user account"""
        fullname, first_name, last_name = self.get_user_names(
            response.get('name')
        )
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'fullname': fullname,
                'first_name': first_name,
                'last_name': last_name}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return {}
        # data = self._user_data(access_token)
        # if not data.get('email'):
        #     try:
        #         emails = self._user_data(access_token, '/emails')
        #     except (HTTPError, ValueError, TypeError):
        #         emails = []
        #
        #     if emails:
        #         email = emails[0]
        #         primary_emails = [
        #             e for e in emails
        #             if not isinstance(e, dict) or e.get('primary')
        #         ]
        #         if primary_emails:
        #             email = primary_emails[0]
        #         if isinstance(email, dict):
        #             email = email.get('email', '')
        #         data['email'] = email
        # return data

    def _user_data(self, access_token, path=None):
        # url = urljoin(self.api_url(), 'user{0}'.format(path or ''))
        # return self.get_json(url, params={'access_token': access_token})
        return {}

