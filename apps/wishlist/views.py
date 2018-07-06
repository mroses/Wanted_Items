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
    if len(users) > 0:
        user = users[0]
        if user.password == request.POST['password']:
            request.session["id"] = user.id
            return redirect('/dashboard')
    messages.error(request, 'entry is not valid')
    return redirect('/')

def dashboard(request):

    logged_user = User.objects.get(id=request.session["id"])
    myitems = Item.objects.filter(users=logged_user)
    other_users = User.objects.exclude(id=logged_user.id)
    other_items = Item.objects.exclude(users = logged_user) #gets all items but excludes items owned by logged user

    context = {
        'myitems': myitems,
        'logged_user': logged_user,
        'other_items': other_items,
        'other_users': other_users,
    }
    return render(request, 'wishlist/dashboard.html', context)
    
def create(request): # add item link from dashboard loads create page
    return render(request, 'wishlist/create.html')

def process(request): #when item is submitted from create page, need to process it before returning to dashboard
    if request.method == "POST":
        item_name = request.POST["item"]
        
        if len(item_name) < 4:
            messages.error(request, 'item name must have more than 3 characters')
            return redirect('/wishlist/create')
        else:
            new_item = Item.objects.create(name=item_name)
            logged_user = User.objects.get(id=request.session["id"])
            logged_user.items.add(new_item)
            
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
'''
def delete(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    messages.success(request, "item deleted")
    return redirect('/dashboard')
'''