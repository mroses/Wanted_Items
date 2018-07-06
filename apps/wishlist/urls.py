from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^wishlist/create$', views.create),
    url(r'^wishlist/process$', views.process),
    url(r'^wishlist/add$', views.add),
    url(r'^logout$', views.logout),
    url(r'wishlist/item/(?P<id>\d+)$', views.item),
    url(r'^wishlist/delete$', views.delete),
    url(r'^wishlist/remove', views.remove)
]