from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import get_user_model
from .forms import uloginform
from django.contrib.auth import authenticate,login,logout
# from django.db.utils import IntegrityError


# Create your views here.
def index(request):
	return render(request,"pages/index.html",{"fname":request.user.username})

def ulogin(request):
	if not request.user.is_authenticated:
		if request.method=="POST":
			fm=uloginform(request=request,data=request.POST)
			if fm.is_valid():
				uname=fm.cleaned_data['username']
				upass=fm.cleaned_data['password']
				user=authenticate(username=uname,password=upass)
				if user is not None:
					login(request,user)
					# print(request.user.username)
					return HttpResponseRedirect('/index/')
		else:
			fm=uloginform()
		return render(request,'pages/login.html',{'form':fm})
	else:
		return HttpResponseRedirect('/index/')

def uafterlogin(request):
	return render(request,'pages/afterlogin.html')

def ulogout(request):
	logout(request)
	return HttpResponseRedirect('/login/')
	

def forpass(request):
	return render(request,'pages/forgotpass.html')

def ureg(request):
	cuser=get_user_model()
	if request.method=="POST":
		fname=request.POST["username"]
		fpasswd=request.POST["password"]
		fphnno=request.POST["MobileNumber"]
		femail=request.POST["uemail"]

		regobj=cuser.objects.create_user(username=fname,password=fpasswd,email=femail,mobno=fphnno)
		regobj.save()
		# print("user created")
		return render(request,"pages/login.html")
	else:
		# print("error")
		return render(request,"pages/register.html")

def forpass(request):
	return render(request,"pages/forgotpass.html")

def dbplumberdb(request):
	if request.method=="POST":
		uname=request.user.username
		uemail=request.user.email
		umobno=request.user.mobno
		faddr=request.POST["Address"]
		fprblm=request.POST["Problem"]

		regobj=Plumberdb1(name=uname,mobno=umobno,email=uemail,addr=faddr,prblm=fprblm)
		regobj.save()
		return HttpResponse("<h1>Booked Sucessfully</h1>")
	else:
		return render(request,"pages/plumber.html")
	
def dbelectrician(request):
	if request.method=="POST":
		uname=request.user.username
		uemail=request.user.email
		umobno=request.user.mobno
		faddr=request.POST["Address"]
		fprblm=request.POST["Problem"]

		regobj=Electriciandb(name=uname,mobno=umobno,email=uemail,addr=faddr,prblm=fprblm)
		regobj.save()
		return HttpResponse("<h1>Booked Sucessfully</h1>")
	else:
		return render(request,"pages/electrician.html")

def dbcook(request):
	if request.method=="POST":
		uname=request.user.username
		uemail=request.user.email
		umobno=request.user.mobno
		faddr=request.POST["Address"]
		fprblm=request.POST["Problem"]

		regobj=Cookdb(name=uname,mobno=umobno,email=uemail,addr=faddr,prblm=fprblm)
		regobj.save()
		return HttpResponse("<h1>Booked Sucessfully</h1>")
	else:
		return render(request,"pages/cook.html")
	