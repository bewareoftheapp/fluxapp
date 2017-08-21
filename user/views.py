from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def get_login_data(request):
    if request.method == "POST":
        return (request.POST['username'],

                request.POST['password'])
    else:
        return None


def login_GET(request):
    return render(request, 'login.html')


def login_POST(request):
    login_data = get_login_data(request)
    auth = authenticate(username=login_data[0], password=login_data[1])
    if auth:
        login(request, auth)
        return redirect('index')
    else:
        data = {'auth_error': True}
        return render(request, 'login.html', data)


def login_page(request):
    if request.method == "POST":
        response = login_POST(request)
    else:
        response = login_GET(request)
    return response


def logout_user(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('login')
