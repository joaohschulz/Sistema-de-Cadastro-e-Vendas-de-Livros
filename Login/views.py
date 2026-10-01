from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm


class RegisterTest(CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class LoginTest(LoginView):
    template_name = 'login.html'
    
class Logout(LogoutView):
    next_page = '/'

