from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *


# Create your views here.
def index(request):
    if request.session.get('id') != None:
        return redirect('/dashboard')
    return render(request, 'wishlist/index.html')

def register(request):
    User.objects.validate(request)
    return redirect('/')

def login(request):
    users = User.objects.filter(username=request.POST['username'])
    print users
    if len(users) > 0:
        user = users[0]
        if user.password == request.POST['password']:
            request.session["id"] = user.id
            return redirect('/dashboard')
    messages.error(request, 'entry is not valid')
    return redirect('/')

def dashboard(request):

    logged_user = User.objects.get(id=request.session["id"])
    print logged_user
   
    context = {
        'logged_user': logged_user,
    }
    
    return render(request, 'wishlist/dashboard.html', context)
    
def create(request): # add item link from dashboard loads create page
    return render(request, 'wishlist/create.html')

def process(request):
    if request.method == "POST":
        item_name = request.POST["item"]
    
        added_by = request.session['id']

        if len(item_name) < 4:
            messages.error(request, 'item name must have more than 3 characters')
            return redirect('/wishlist/create')
        else:
            new_item = Item.objects.create(name=item_name, creator=User.objects.get(id=added_by))

            logged_user = User.objects.get(id=request.session["id"])
            creator = logged_user
            creator.items.add(new_item)
                  
        return redirect('/dashboard')

def item(request, id): 
    item = Item.objects.get(id=id)
    user = User.objects.filter(items=item)
    context = {
        'item': item,
        'user': user
    }
    return render(request, 'wishlist/item.html', context)#loads specific item page

def add(request): #add item to user.session's list, remove from others list
    return redirect('/dashboard')

def remove(request): #remove from user list, add to others list
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request):
    return redirect('/dashboard')
