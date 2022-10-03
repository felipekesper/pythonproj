from django.urls import path, include
from ctable import views

urlpatterns = [
	path("",views.home,name='home'),
	path("insert/",views.insert,name='insert'),
]