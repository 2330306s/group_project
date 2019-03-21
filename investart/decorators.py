#Custom decorators to check authentication and user types

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

#Redirecting to homepage if not authenticated
def homepage_if_not_auth(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='index'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and (u.is_dev or u.is_inv),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

#Redirecting to developer login page if not logged in as developer
def dev_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='dev_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_dev,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

#Redirecting to investor login page if not logged in as investor
def inv_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='inv_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_inv,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
