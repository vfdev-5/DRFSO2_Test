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
For that user need to login :


### 3) Access api protected resources






## Login user

Idea is to login with
- a local account (e.g. userone:123)
- a social network account (Github)

and get a access_token/expires/provider from OAuth2 providers

## Register user

- for a social network account it work automatically

