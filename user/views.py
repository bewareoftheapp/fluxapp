'''User views.'''

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from . import forms, models


def get_login_data(request):
    '''Get credentials information from POST message or return None.'''
    if request.method == "POST":
        response = (request.POST['username'],
                    request.POST['password'])
    else:
        response = None
    return response


def login_GET(request):
    '''Respond a GET request to login page.'''
    return render(request, 'login.html')


def login_POST(request):
    '''Respond a POST request to login page.'''
    login_data = get_login_data(request)
    auth = authenticate(username=login_data[0], password=login_data[1])
    if auth:
        login(request, auth)
        response = redirect('index')
    else:
        data = {'auth_error': True}
        response = render(request, 'login.html', data)
    return response


def login_page(request):
    '''Respond login page.'''
    if request.user.is_authenticated():
        response = redirect('index')
    elif request.method == "POST":
        response = login_POST(request)
    else:
        response = login_GET(request)
    return response


def logout_user(request):
    '''Logout user.'''
    if request.user.is_authenticated():
        logout(request)
    return redirect('login')


def new_user(request):
    '''Start the new user process generating a registration token.'''
    data = {'user': request.user}
    if request.method == "GET":
        data['registration_form'] = forms.RegistrationTokenForm()
        response = render(request, 'new_user.html', data)
    else:
        registration_form = forms.RegistrationTokenForm(request.POST)
        try:
            response = render_registration_token(request, registration_form.save())
        except ValueError:
            data['registration_form'] = registration_form
            response = render(request, 'new_user.html', data)
    return response


def render_registration_token(request, registration_token):
    '''Render a user.models.RegistrationToken.'''
    data = {
        'user': request.user,
        'host': request.META['HTTP_HOST'],
        'registration_token': registration_token
    }
    return render(request, 'registration_token.html', data)


def get_registration_token(request, reg_token_id):
    '''Selects and render a user.models.RegistrationToken.'''
    registration_token = get_object_or_404(models.RegistrationToken, id=reg_token_id)
    return render_registration_token(request, registration_token)


def validate_token(request, registration_token):
    '''Validate registration token and email.

    Return (HttpResponse):
        Rendered user form if token and email is valid.
        Rendered token validation form if token or email is invalid.'''

    data = {}
    if registration_token.email == request.POST['email']:
        data['user_form'] = forms.UserForm()
        data['user_token'] = registration_token.token
    else:
        data['registration_token'] = registration_token
        data['email_error'] = True
    return render(request, 'register_user.html', data)


def register_user(request):
    '''Register a new user to system.'''
    data = {}
    if request.method == "GET" and request.GET.get('token'):
        registration_token = get_object_or_404(models.RegistrationToken, token=request.GET['token'])
        data['registration_token'] = registration_token
        response = render(request, 'register_user.html', data)
    elif request.method == "POST" and request.POST.get('token'):
        response = validate_token(request, get_object_or_404(models.RegistrationToken,
                                                             token=request.POST['token']))
    elif request.method == "POST" and request.POST.get('username'):
        user_form = forms.UserForm(request.POST)
        try:
            user_form.save(commit=False)
            user = User.objects.create_user(**user_form.cleaned_data)
            user.save()

            registration_token = models.RegistrationToken.objects.get(
                token=request.POST.get('user_token'))
            registration_token.active = False
            registration_token.save()

            data['new_user'] = user
            response = render(request, 'register_user.html', data)
        except ValueError:
            data['user_form'] = user_form
            response = render(request, 'register_user.html', data)
    else:
        response = render(request, 'register_user.html')
    return response
