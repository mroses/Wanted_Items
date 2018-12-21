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
            if valid == True:
                User.objects.create(name=request.POST['name'], username=request.POST['username'], password=request.POST['password'], 
                )
                messages.success(request, 'registered success')

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=500)
    confirm_pw = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    items = models.ForeignKey(Item, related_name="wishlist_items")
    creator = models.ForeignKey(User, related_name="wishlist_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
