from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def account(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/account.html', context_dict)

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/about.html', context_dict)
    return response

def index(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/index.html', context_dict)
    return response

def contact(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/contact.html', context_dict)
    return response

def dev_login(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dev = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, dev)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'investart/dev_login.html', context_dict)
        

def inv_login(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        inv = authenticate(username=username, password=password)

        if inv:
            if inv.is_active:
                login(request, inv)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'investart/inv_login.html', context_dict)

def mod_login(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mod = authenticate(username=username, password=password)

        if mod:
            if mod.is_active:
                login(request, mod)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'investart/mod_login.html', context_dict)

def dev_signup(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/dev_signup.html', context_dict)
    return response

def inv_signup(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/inv_signup.html', context_dict)
    return response

def developer(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/developer.html', context_dict)
    return response

def investor(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/investor.html', context_dict)
    return response

def moderator(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/moderator.html', context_dict)
    return response

def get_server_side_cookie(request, cookie, default_val = None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    if(datetime.now() - last_visit_time).days > 0:
        visits = visits +1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    request.session['visits'] = visits
