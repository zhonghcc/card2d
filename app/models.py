from django.db import models

# Create your models here.
class Card(models.Model):
	username = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	qq = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	position = models.CharField(max_length=200)
	tel = models.CharField(max_length=200)

