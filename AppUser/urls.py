from django.contrib.auth.views import LogoutView
from django.urls import path
from AppUser.views import *


urlpatterns = [
    path('login/',login_request, name='AppUserLogin'),
    path('Register/', register, name= 'AppUserRegister'),
    path('logout/', LogoutView.as_view(template_name='AppUser/logout.html'), name= 'AppUserLogout'),
    path('editar/', edit_user, name='AppUserEdit'),
]
