from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def HomeView(request):
    template_name = 'firstapp/home.html'
    return render(request,template_name)

def SignUpView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email Already Used")
            return redirect('signup')
        else:
            user = User.objects.create_user(username = email, password = password)
            user.save()
            send_mail('Signed In', f'You have Signed in using{email}','bsagar321@gmail.com',[email])
            messages.success(request, f'Account Created for {email}')
    template_name = 'firstapp/signup.html'
    return render(request,template_name)

def LoginView(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are Logged in as {u}!!')
            send_mail('Logged In', f'You have logged in using{u}','bsagar321@gmail.com',[u])
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    template_name = 'firstapp/login.html'
    return render(request,template_name)

def LogoutView(request):
    logout(request)
    return redirect('home')