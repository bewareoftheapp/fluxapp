from django.shortcuts import render
from django.contrib.auth import authenticate, login


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
        return render(request, 'login.html')
    else:
        data = {'auth_error': True}
        return render(request, 'login.html', data)


def login_page(request):
    if request.method == "POST":
        response = login_POST(request)
    else:
        response = login_GET(request)
    return response
