from django.db import models

# Create your models here.

class Cliente(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Client(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GEN = [(MALE, 'Male'),(FEMALE, "Female")]
	name = models.CharField(max_length=50)
	sur_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	gender = models.CharField(max_length=6,choices=GEN)