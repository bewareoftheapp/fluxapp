from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        result = render(request, 'index.html')
    else:
        result = redirect('login')
    return result
