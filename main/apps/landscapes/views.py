from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'landscapes/index.html')

def show(request, number):
    request.session.clear()
    if 1 <= int(number) <= 10:
        landscapes = {'snow'}
    elif 11 <= int(number) <= 20:
        landscapes = {'desert'}
    elif 21 <= int(number) <= 30:
        landscapes = {'forest'}
    elif 31 <= int(number) <= 40:
        landscapes = {'vineyard'}
    elif 41 <= int(number) <= 50:
        landscapes = {'tropical'}
    else:
        request.session['message'] = "I told you to use a number between 1 and 50, Ben."
        landscapes = {'tyrion'}
    return render(request, 'landscapes/show.html', {'landscapes': landscapes})
