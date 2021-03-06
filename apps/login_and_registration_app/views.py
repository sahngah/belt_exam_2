from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login_and_registration_app/page.html')

def register(request):
    if request.method == "POST":
        variable1 = User.objects.register(request.POST)
        if 'user' in variable1:
            context = {
            'user' : variable1['user']
            }
            request.session['user'] = variable1['user'].id
            return redirect('dashboard:index')
        else:
            for random in variable1['errors']:
                messages.error(request, random)
            return redirect('/')

def login(request):
    if request.method == "POST":
        variable2 = User.objects.login(request.POST)
        if 'user' in variable2:
            context = {
            'user' : variable2['user']
            }
            request.session['user'] = variable2['user'].id
            return redirect('dashboard:index')
        else:
            messages.error(request, variable2['errors'])
            return redirect('/')

def success(request):
    pass
