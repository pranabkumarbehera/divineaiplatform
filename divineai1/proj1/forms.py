from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import *


class uloginform(AuthenticationForm):
	username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
	password=forms.CharField(label=_("Password"),
							strip=False,
							widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))

# class Plumbermdlform(forms.ModelForm):
# 	class Meta:
# 		model=Plumbermdl
# 		fields=['id','addr','prblm','img']
# 		widgets={'addr':forms.TextInput(attrs={'class':'form-control'}),
# 				'prblm':forms.Textarea(attrs={'class':'form-control'})}
# 		labels={'img':'','addr':'Address','prblm':'Problem'}