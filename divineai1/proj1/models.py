from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	mobno=models.CharField(max_length=50)

class Electriciandb(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	mobno=models.IntegerField()
	addr=models.CharField(max_length=600)
	prblm=models.CharField(max_length=800)
	date=models.DateTimeField(auto_now_add=True)


class Cookdb(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	mobno=models.IntegerField()
	addr=models.CharField(max_length=600)
	prblm=models.CharField(max_length=800)
	date=models.DateTimeField(auto_now_add=True)


class Plumberdb1(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField(max_length=100)
	mobno=models.IntegerField()
	addr=models.CharField(max_length=600)
	prblm=models.CharField(max_length=800)
	date=models.DateTimeField(auto_now_add=True)

