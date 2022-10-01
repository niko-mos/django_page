from django.urls import path
from users.views import home, order, primeri, zayavka, register, login, profile
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('primeri/', primeri, name='primeri'),
    path('zayavka/', zayavka, name='zayavka'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LoginView.as_view(template_name='users/logout.html'), name='logout'),


    #why? gotta define in views -> then reference here
]