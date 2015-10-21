# A test of [django-rest-framework-social-oauth2](https://github.com/PhilipGarnero/django-rest-framework-social-oauth2/blob/master/rest_framework_social_oauth2)


## Idea :
- Rest Api with open/protected resources :
    - Available entry points :
        - open : /api/, /api/register/
        - protected : /api/protected/
- Users :
    - local
    - social
- Client applications: a) local website, b) mobile app (curl + web browser)
    - register new local user
    - access protected resources

## Server backend
- OAuth2 application : client type is 'Confidental' and authorization grant type is 'Resource owner password-based'


## Mobile app

### 1) Obtain the access token for a github user
Open web browser with URL :
```
/auth/login/github/?next=/profile/
```
Authorize the usage of the user information by the server.
The final redirection will contain the parameters: access_token, backend, expires
```
/profile/?access_token=<token>&backend=<backend>&expires=<expires>
```
Note: a new user will be created automatically

### 2.1) Create new local user
Send POST request to '/api/register/' with parameters :
- username=<username>
- password=<password>
- email=<email>

```
curl -X POST -d "username=${username}&password=${password}&email=${email}" /api/register/
```

Note: user is identified by its unique username

### 2.2) Obtain the access token for a local user
Send POST request to '/auth/token/' with parameters :
- username=<username>
- password=<password>
- grant_type=password
- client_id=<client_id>
- client_secret=<client_secret>

```
curl -X POST -d "client_id=${client_id}&client_secret=${client_secret}&grant_type=password&username=${username}&password=${password}" ${URL}
```

### 3) Access api protected resources
#### For a local user :
Insert "Authorization: Bearer <token>" to the header and send a request to the url
```
curl -v -H "Authorization: Bearer <token>" /api/protected/
```

#### For a social network user :
Insert "Authorization: Bearer github <token>" to the header and send a request to the url
```
curl -v -H "Authorization: Bearer github <token>" /api/protected/
```

## Local web site

### 1) Obtain the access token for a github user
For that user need to login :
Html part :
```
<a href="/auth/login/github/?next=/">Login with Github</a>
```
Django part :
It is possible to insert access token and backend as templates to views.

```
user = request.user
if user.is_authenticated:
    try:
        # get the last login provider
        provider = request.session['social_auth_last_login_backend']
        social = user.social_auth.get(provider=provider)
        access_token = social.extra_data['access_token']
        expires = social.extra_data['expires']
    except KeyError:
        # This is a local user without social network backend


context = {
    "access_token": access_token,
    "provider": provider,
    "expires": expires,
}
```

### 2.1) Create new local user
It can be done with a simple html form

### 2.2) Obtain the access token for a local user

For that user need to login : configure url to django.contrib.auth.views.login with a custom template html
```
url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
```
and redirect the link to the main page.

In the main page django view code to get access token should be separated for social and local users
```
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
```

In the method 'get_or_create_token' find not expired access tokens using 'oauth2_provider.models.AccessToken' :
```
application = Application.objects.get(name="Local OAuth2 Server with Password")
tokens = AccessToken.objects.filter(user=user, expires__gt=datetime.now(), application=application)
```
if no tokens found then create one with a refresh token

### 3) Access api protected resources
This can be done using ajax or whatever other tools that can send requests to the urls. For example, using jquery $.ajax :
#### For a local user :
```
var headers = {"Authorization": "Bearer " + token};
var request = $.ajax({
    url: '/api/protected/',
    method: "GET",
    headers: headers
}).done(function( msg ) {
    // Do something with the resulting message object
});
```
#### For a social network user :
```
var headers = {"Authorization": "Bearer github " + token};
var request = $.ajax({
    url: '/api/protected/',
    method: "GET",
    headers: headers
}).done(function( msg ) {
    // Do something with the resulting message object
});
```




## Open questions :

- How to issue a token for a local user
-> Create token using Application, AccessToken etc

- Mobile part should display only its own access_tokens
-- need convert 3rdparty tokens to local tokens

- How to use refresh tokens
- How to remove expired tokens, https://github.com/evonove/django-oauth-toolkit/issues/148

- Mobile / API / Django / 3rd party OAuth workflow, http://stackoverflow.com/questions/27051209/oauth2-token-authentication-using-django-oauth-toolkit-and-python-social-auth

