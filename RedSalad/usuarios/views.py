from django.shortcuts import render, redirect, _get_queryset
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from usuarios.models import Productor, Usuario, Cliente
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView
from usuarios.forms import ProductorForm
from django.http.response import HttpResponseRedirect
from django import forms
from django.forms.forms import Form

# Create your views here.
class IndexView(TemplateView):
    
    def get_template_names(self):
        
        try:        
            usuarioQ=Usuario.objects.filter(user__id=self.request.user.id)
            
        except:
            usuarioQ=2
        print(self.request.user)
        print(usuarioQ)

        
        try:
            productor = Productor.objects.filter(usuario=usuarioQ)
        
        except:
            productor = 1
            
        try:
            cliente = Cliente.objects.filter(usuario=usuarioQ)
        
        except:
            cliente = 1
            
        if cliente==1 and productor==1:
            template_name = 'index_primera_vez.html'
        
        else:
            template_name='index.html'
            
            
            
        return template_name  


            
        
    
    
class LoginViewL(TemplateView):
    template_name='login.html'

def LogOut(request):
    logout(request)
    return redirect("/")


class PerfilProductorView(DetailView):
    context_object_name = 'productor_perfil'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PerfilProductorView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        usuarioQ=Usuario.objects.filter(user=self.request.user)
        return Productor.objects.filter(usuario=usuarioQ)
    
    

class ProductorCrear_Usuario(CreateView):
    model = Usuario
    fields = ['telefono','pais','ciudad','provincia','codigo_postal','direccion']
    success_url = '/usuario/nuevoproductor/2'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        
        return redirect('/usuario/nuevoproductor/2')


class SignupForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = ['alias_empresa','bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': '4'})
        }

class ProductorCrear_Productor(CreateView):
    model = Productor
    form_class=SignupForm
#    fields = ['alias_empresa','bio']
    success_url = '/thanks/'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.usuario = Usuario.objects.filter(user_id=self.request.user.id)[0]
        instance.save()
        
        return redirect('/thanks')
    



class ProductorView(FormView):
    template_name = 'contact.html'
    form_class = ProductorForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return super(ProductorView, self).form_valid(form) 


    

    
