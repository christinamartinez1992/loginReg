from django.conf.urls import url, include
from django.contrib import admin
from . import views


# These will be tied into your views.py
urlpatterns = [
	url(r'^$',views.index),
	url(r'^users$', views.register),
	url(r'^success$', views.success),
	url(r'^login$', views.login),

]
