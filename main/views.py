from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated():
        data = {'user': request.user}
        result = render(request, 'index.html', data)
    else:
        result = redirect('login')
    return result
