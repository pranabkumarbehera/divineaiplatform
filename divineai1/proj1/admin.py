from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class cuseradmin(admin.ModelAdmin):
	list_display=['id','username','email','mobno','date_joined']

UserAdmin.fieldsets += ("Custom fields set",{'fields':('mobno',)}),

@admin.register(Plumberdb1)
class Plumberadmin(admin.ModelAdmin):
	list_display=['id','name','email','mobno','addr','date','prblm']


@admin.register(Electriciandb)
class Electricianadmin(admin.ModelAdmin):
	list_display=['id','name','email','mobno','addr','date','prblm']

@admin.register(Cookdb)
class Cookadmin(admin.ModelAdmin):
	list_display=['id','name','email','mobno','addr','date','prblm']