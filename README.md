# Django Ninja Auth: Use Django authorization infrastructure with Django Ninja

Django Ninja Auth is a minimalistic python package that leverages the funcionalities of `django.contrib.auth` to backend-only [Django](https://www.djangoproject.com/) projects that use the exceptional [Django Ninja](https://django-ninja.rest-framework.com/).

## Install
1. `pip install django-ninja-auth` (⚠️ Not ready!).
2. Add the router to your `NinjaAPI`. Assuming you created a project according to [Django Ninja's tutorial](https://django-ninja.rest-framework.com/tutorial/) just follow this template in `api.py`:
```python
from ninja import NinjaAPI
from ninja_auth.api import router as auth_router

api = NinjaAPI()
api.add_router('/auth/', auth_router)
```
3. Build the front-end infrastructure to interact with `your-api.com/api/auth/` 🚀.

## Documentation
If you followed the steps above, everything should be documented in your OpenAPI/Swagger UI under `your-api.com/api/docs`. No unnecessary documentation here 😎.

## CSRF
Unfortunately, Django Ninja will [force you to use CSRF protection](https://django-ninja.rest-framework.com/tutorial/csrf/). It is your responsibility to build a front-end that takes care of this, adding it in the API's schema does not make sense. If you ask me, I'd just use `SESSION_COOKIE_SAMESITE = 'strict'` and `SESSION_COOKIE_HTTPONLY = True` (default) and forget about CSRF attacks. "But there are old browsers that... 😭😭"   - If your cookies get stolen because you use Netscape it's not my fault.

## Password Reset Email
When you call `/api/auth/request_password_reset/` you only need to provide an email address. If the address corresponds to an actual user, Django will send an email to that address with a token to reset the password of the user (of course, you need to configure email sending in your `settings.py`). By default, the email is built using a [horrendous template](https://github.com/django/django/blob/main/django/contrib/admin/templates/registration/password_reset_email.html) provided by the `django.contrib.auth` app. If you are not using such app, Django will complain because the template does not exist. My recommendation is to build your own beautiful template and place it in `registration/password_reset_email.html` under some of your *templates directories*. To build that template you can use the follwing variables:
- `protocol`: usually `http` or `https`.
- `domain`: whatever was before `/api/auth/request_password_reset/` when the request was made.
- `uid`: the user's id in base64.
- `user`: an object containing data of the user. You can retrieve the username via `{{ user.get_username }}`.
- `site_name`: your site's name.
- `token`: the reset token
