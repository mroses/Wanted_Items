from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

# Create your models here.
class UserManager(models.Manager):
    def validate(self, request):
        if request.method == "POST":
            valid = True
            if len(request.POST['name']) < 3:
                valid = False
                messages.error(request, "name must be at least 3 characters")
            if len(request.POST['username']) < 3:
                valid = False
                messages.error(request, "username must be at least 3 characters")
            if request.POST['password'] != request.POST['confirm_pw']:
                valid = False
                messages.error(request, "passwords do not match")
            if len(request.POST['password']) < 8:
                valid = False
                messages.error(request, "password must be at least 8 characters")
            if request.POST['date_hired'] == "":
                valid = False
                messages.error(request, "must enter date")
            if valid == True:
                User.objects.create(name=request.POST['name'], username=request.POST['username'], password=request.POST['password'], date_hired=request.POST['date_hired'])
                messages.success(request, 'registered success')

class Item(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    date_hired = models.DateField()
    items = models.ManyToManyField(Item, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #def __str__(self):
    #    return self.item.name + " " + self.name + " " + self.item.created_at.str()


'''
SCRATCH PAPER:
this_item = Item.objects.get(id=1)
this_user = User.objects.get(id=2)
this_user.items.add(this_item)

this_item.users.add(this_user)
this_user.items.add(this_item)
this_item.users.all() #returns all users of a given item

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #def __str__(self):
    #    return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    #user = models.ForeignKey(User, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    item = models.ForeignKey(Item, related_name="wishlist")
    user = models.ForeignKey(User, related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''