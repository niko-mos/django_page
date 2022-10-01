from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from . import models
from django.core.mail import send_mail

from . forms import UserRegisterForm
# Create your views here.

def home(request):
#    return render(request, "index.html", {})
    template = loader.get_template('users/index.html')
    return HttpResponse(template.render())
     

def order(request):
    template = loader.get_template('users/order.html')
    return HttpResponse(template.render())

def primeri(request):
    template = loader.get_template('users/primeri.html')
    return HttpResponse(template.render())

def zayavka(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data = {'name' : name,
                'email': email, 
                'message': message
               }
        
        message = '''
        New message: {}

        From: {}

        '''.format(data['message'], data['email'])
#        send_mail(data['name'], message, '', ['logo.order.io@gmail.com'])
        ins = models.Contact(name=data['name'], email=data['email'], message=data['message'])
        ins.save()
        
    return render(request, 'users/zayavka.html', {})

#    template = loader.get_template('users/zayavka.html')
#    return HttpResponse(template.render())

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Ваш аккаунт создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()


#    template = loader.get_template('users/register.html')
#    return HttpResponse(template.render())
    return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Ваш аккаунт создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()


#    template = loader.get_template('users/register.html')
#    return HttpResponse(template.render())
    return render(request, 'users/login.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')