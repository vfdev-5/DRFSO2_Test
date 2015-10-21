# Python
from datetime import datetime, timedelta

# OAuth2 provider
from oauth2_provider.models import AccessToken, Application, RefreshToken

# OAuthlib
from oauthlib.common import generate_token

def get_or_create_token(user):
    print "get_or_create_token for user : ", user


    try:
        # DEBUG Show all tokens
        # print "DEBUG Show all tokens"
        # tokens = AccessToken.objects.all()
        # print "Found ", len(tokens), " tokens"
        # for token in tokens:
        #     print "Token : ", token.id, token.user, token.token, token.application, token.expires, token.scope
        #     refresh_token = RefreshToken.objects.get(access_token=token)
        #     print "Refresh token : ", refresh_token.id, refresh_token.user, refresh_token.application, refresh_token, refresh_token.access_token
        # # DEBUG Show all tokens
        # print "ENDDEBUG Show all tokens"


        application = Application.objects.get(name="Local OAuth2 Server with Password")

        tokens = AccessToken.objects.filter(user=user, expires__gt=datetime.now(), application=application)
        print "Found ", len(tokens), " tokens"
        for token in tokens:
            print "Token : ", token.id, token.user, token.token, token.application, token.expires, token.scope
            refresh_token = RefreshToken.objects.get(access_token=token)
            print "Refresh token : ", refresh_token.id, refresh_token.user, refresh_token.application, refresh_token, refresh_token.access_token

        if len(tokens) == 0:
            print "Create new token"
            expires=datetime.now() + timedelta(seconds=36000)
            scope="read write"
            token = AccessToken.objects.create(user=user, application=application, expires=expires, token=generate_token(), scope=scope)
            refresh_token = RefreshToken.objects.create(user=user, application=application, token=generate_token(), access_token=token)
            print "Created token : ", token.id, token.user, token.token, token.application, token.expires, token.scope
            print "with a Refresh token : ", refresh_token.id, refresh_token.user, refresh_token.application, refresh_token, refresh_token.access_token
            return token
        else:
            # get the first
            print "Return the first found token"
            return tokens[0]
    except:
        # do something
        print "Exception is thrown"
        return None




def get_or_create_token2(user):
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
    # uri = u'/auth/token/'
    # body = None
    # headers = None
    # token_request = Request(uri, http_method='POST', body=body, headers=headers)
    #
    # oauth_core = TokenView.get_oauthlib_core() # Problem with classmethod
    # server = oauth_core.server
    # print "Server : ", server
    # token_handler = server.default_token_type
    # access_token = token_handler.create_token(token_request)
    # provider = "Local"



    # client_id="client_id"
    # client_secret="client_secret"
    # username = user.username
    # password = user.password # Problem with password which is encrypted
    #
    # url = reverse('token')
    # data = {
    #     'client_id': client_id,
    #     'client_secret': client_secret,
    #     'username': username,
    #     'password': password
    # }
    # print data
    # headers = {'Content-Type': 'application/json'}

    # r = requests.post(url, data=json.dumps(data), headers=headers)
    # print r

    pass



