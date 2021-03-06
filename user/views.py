'''User views.'''

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.core.urlresolvers import reverse

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
    nextPage = request.GET.get('next')
    data = {}
    if nextPage:
        data['next'] = nextPage
    return render(request, 'login.html', data)


def login_POST(request):
    '''Respond a POST request to login page.'''
    user_name, password = get_login_data(request)
    auth = authenticate(username=user_name, password=password)
    if auth:
        login(request, auth)
        nextPage = request.GET.get('next')
        response = redirect(str(nextPage) if nextPage else 'index')
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


@staff_member_required(login_url='login')
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


@staff_member_required(login_url='login')
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
        data['user_form'] = forms.UserForm(initial={'email': str(registration_token.email)})
        data['user_token'] = registration_token.token
    else:
        data['registration_token'] = registration_token
        data['email_error'] = True
    return render(request, 'register_user.html', data)


def register_user(request):
    '''Register a new user to system.'''
    if request.user.is_authenticated():
        data = {
            'err_msg': 'Para registrar um novo usuário você precisa sair de sua conta.',
            'btn_msg': 'Sair',
            'btn_href': reverse('logout')
        }
        return render(request, 'oops.html', data)

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


@staff_member_required(login_url='login')
def active_tokens(request):
    '''Respond active tokens.

    If token is active then the invitation is pending.'''
    data = {
        'host': request.META['HTTP_HOST'],
        'active_tokens': models.RegistrationToken.objects.filter(active=True)
    }
    return render(request, 'active_tokens.html', data)


def handle_staff_status(request, prefix, status):
    '''Add/remove staff status of users.'''
    user_ids = [key.split('_')[1]
                for key in request.POST.keys()
                if key.startswith(prefix + '_') and request.POST[key]]

    if not user_ids:
        return

    users = User.objects.filter(id__in=user_ids)
    for user in users:
        user.is_staff = status
        user.save()


@staff_member_required(login_url='login')
def staff_users(request):
    '''Manage staff users.

    Add or remove user's staff credential.'''

    if request.method == "GET":
        users = User.objects.exclude(first_name__exact="")
        data = {
            'staff_users': users.filter(is_staff=True),
            'non_staff_users': users.filter(is_staff=False)
        }
        response = render(request, 'staff_users.html', data)
    else:
        handle_staff_status(request, 'add', True)
        handle_staff_status(request, 'remove', False)
        response = redirect('staff_users')

    return response
