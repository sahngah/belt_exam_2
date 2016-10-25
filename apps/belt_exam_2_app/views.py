from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages
from ..login_and_registration_app.models import User

# Create your views here.
def index(request):
    user = User.objects.get(id=request.session['user'])
    context={
    'user': user,
    'user_on' : user.item_created.all(),
    'user_on_on': user.items_added.all(),
    'user_off': Item.objects.exclude(user=user).exclude(users=user)
    }
    return render(request, 'belt_exam_2_app/page.html', context)

def create(request):
    return render(request, 'belt_exam_2_app/create.html')

def additem(request):
    if request.method == "POST":
        itemlist = Item.objects.additem(request.POST, user=User.objects.get(id=request.session['user']))
        if 'item' in itemlist:
            context={
            'item':itemlist['item']
            }
            return redirect('dashboard:index')
        else:
            for error in itemlist['errors']:
                messages.error(request,error)
        return redirect('dashboard:create')

def details(request, id):
    item = Item.objects.get(id=id)
    context ={
    'item' :item
    }
    return render(request, 'belt_exam_2_app/details.html', context)

def join(request, id):
    item=Item.objects.get(id=id)
    user=User.objects.get(id=request.session['user'])
    item.users.add(user)
    return redirect('dashboard:index')

def logout(request):
    request.session.clear()
    return redirect('login:index')

def remove(request, id):
    item=Item.objects.get(id=id)
    user=User.objects.get(id=request.session['user'])
    item.users.remove(user)
    return redirect('dashboard:index')

def delete(request,id):
    item=Item.objects.get(id=id).delete()
    return redirect('dashboard:index')
