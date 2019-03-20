from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def homepage_if_not_auth(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='index'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.is_dev or u.is_inv or u.is_mod),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def dev_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='dev_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_dev,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def inv_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='inv_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_inv,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def mod_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='mod_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_mod,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
