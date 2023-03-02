from django.shortcuts import render

def register(request, *args, **kwargs):
    return render(request, 'register.html', {})
def login(request):
    return render(request, 'login.html', {})
