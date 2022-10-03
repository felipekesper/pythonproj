from django.urls import path
from . import views

urlpatterns = [
	path('accounts/',views.accounts,name='accounts'),
	path('logout/',views.logoutaccount,name='logoutaccount'),
	path('login/', views.loginaccount,name='loginaccount'),
]

