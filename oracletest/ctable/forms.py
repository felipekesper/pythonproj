from django import forms
from django.forms.widgets import Select

class ContactForm(forms.Form):
	MALE = 'Male'
	FEMALE = 'Female'
	GEN = [(MALE, 'Male'),(FEMALE, "Female")]
	name = forms.CharField(label='Name:',max_length=50)
	sur_name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	gender = forms.CharField(widget=forms.Select(choices=GEN))
