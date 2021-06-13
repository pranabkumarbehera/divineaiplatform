from django.urls import path
from . import views

urlpatterns = [
		path("index/",views.index,name="index"),
		path("login/",views.ulogin,name="login"),
		path("forgotpassword/",views.forpass,name="forpswd"),
		path("plumber/",views.dbplumberdb,name="plumber"),
		path("electrician/",views.dbelectrician,name="electrician"),
		path("cook/",views.dbcook,name="cook"),
		path("register/",views.ureg,name="ureg"),
		path("afterlogin/",views.uafterlogin,name="afterlogin"),
		path('logout/',views.ulogout,name='logout'),
]