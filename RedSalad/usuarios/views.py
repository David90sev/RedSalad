from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import logout

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'
    
class LoginViewL(TemplateView):
    template_name='login.html'

def LogOut(request):
    logout(request)
    return redirect("/")