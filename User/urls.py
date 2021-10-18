from django.urls import path,include
#from employee_register import views
from . import views
#from views import register_request, login_request,logout_request

urlpatterns = [
    path("",views.Home,name='home'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
]