from django.shortcuts import render

def register(request, *args, **kwargs):
    return render(request, 'register.html', {})