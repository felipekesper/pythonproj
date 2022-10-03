from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente, Client
from .forms import ContactForm

# Create your views here.

def insert(request):
	if request.method == 'POST':
		c = Client()
		c.name = request.POST.get('name')
		c.sur_name = request.POST.get('sur_name')
		c.email = request.POST.get('email')
		c.gender = request.POST.get('gender')
		c.save()		
	return render(request,'./insert.html')

def home(request):
	cform = ContactForm()
	context = {'cform':cform}
	return render(request,'./home.html',context)