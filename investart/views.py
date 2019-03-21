from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from investart.forms import ProjectForm, ContactForm, DevForm, InvForm, DevProfileForm, InvProfileForm
from investart.models import NewUser, Project, Contact
from investart.decorators import homepage_if_not_auth, dev_required, inv_required
from datetime import datetime

@homepage_if_not_auth
def account(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/account.html', context_dict)
    return response

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/index.html', context_dict)
    return response

def about(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/about.html', context_dict)
    return response

def contact(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return thank_you(request)
    return render(request, 'investart/contact.html',{'form':form})

def thank_you(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/thank_you.html', context_dict)
    return response

def dev_login(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        dev = authenticate(username=username, password=password)

        if dev:
            if dev.is_active:
                login(request, dev)
                return HttpResponseRedirect(reverse('developer'))
            else:
                return render(request, 'investart/bad_login.html', context_dict)
        else:
            return render(request, 'investart/bad_login.html', context_dict)
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
                return HttpResponseRedirect(reverse('investor'))
            else:
                return render(request, 'investart/bad_login.html', context_dict)
        else:
            return render(request, 'investart/bad_login.html', context_dict)
    else:
        return HttpResponseRedirect(reverse('investor'))

def dev_signup(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    registered = False
    
    if request.method == 'POST':
        dev_form = DevForm(data=request.POST)
        dev_profile_form = DevProfileForm(data=request.POST)

        if dev_form.is_valid() and dev_profile_form.is_valid():
            dev = dev_form.save()
            dev.set_password(dev.password)
            dev.save()
            dev_profile = dev_profile_form.save(commit=False)
            dev_profile.dev = dev
            dev_profile.save()
            registered = True
    else:
        dev_form = DevForm()
        dev_profile_form = DevProfileForm()

    context_dict = {'dev_form': dev_form, 'dev_profile_form': dev_profile_form, 'registered': registered}
    return render(request, 'investart/dev_signup.html', context_dict)

def inv_signup(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    registered = False
    
    if request.method == 'POST':
        inv_form = InvForm(data=request.POST)
        inv_profile_form = InvProfileForm(data=request.POST)

        if inv_form.is_valid() and inv_profile_form.is_valid():
            inv = inv_form.save()
            inv.set_password(inv.password)
            inv.save()
            inv_profile = inv_profile_form.save(commit=False)
            inv_profile.inv = inv
            inv_profile.save()
            registered = True
    else:
        inv_form = InvForm()
        inv_profile_form = InvProfileForm()

    context_dict = {'inv_form': inv_form, 'inv_profile_form': inv_profile_form, 'registered': registered}
    return render(request, 'investart/inv_signup.html', context_dict)

@login_required
@dev_required
def developer(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/developer.html', context_dict)
    return response

@login_required
@inv_required
def investor(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/investor.html', context_dict)
    return response

@homepage_if_not_auth
def show_project(request, project_name_slug):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    try:
        project = Project.objects.get(slug=project_name_slug)
        context_dict['project'] = project
    except:
        context_dict['project'] = None
    return render(request, 'investart/project.html', context_dict)

@homepage_if_not_auth
@dev_required
def add_project(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return developer(request)
    return render(request, 'investart/add_project.html', {'form':form})

def password_reset(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/password_reset_form.html', context_dict)
    return response

def password_reset_done(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/password_reset_done.html', context_dict)
    return response

def password_reset_confirm(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/password_reset_confirm.html', context_dict)
    return response

def password_reset_complete(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'investart/password_reset_complete.html', context_dict)
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
