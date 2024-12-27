from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Registro
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .models import programacion, Ingenieria, formulario, Contacto
from.forms import Ingenieriaformulario, Registro

def about(request):
    return HttpResponse('ABOUT')


def inicio(request):
    return render(request,'MYAPP/index.html')

def programacion(request): 
       
    return render(request, 'MYAPP/programacion.html', {"programacion":programacion})
    

def Ingenieria(request):
    return render(request, 'MYAPP/Ingenieria.html', {"Ingenieria":Ingenieria})

def Contacto(request):
    return render(request,'MYAPP/Contacto.html', {"Contacto":Contacto})

#Formulario

def formulario_api(request):   

    if request.method == "POST" :
        Ingenieria_form = Ingenieriaformulario(request.POST)
        print(Ingenieria_form)

        if Ingenieria_form.is_valid():
            info_limpia = Ingenieria_form.cleaned_data
            
            print(info_limpia)
           
    else:
        Ingenieria_form = Ingenieriaformulario()
   

    contexto = {"form": Ingenieria_form}
      
    return render(request, 'MYAPP/Forms/formulario.html', contexto)

#Registro 

class RegistroView(FormView):
    template_name = 'registro.html'
    form_class = Registro
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroView, self).get(*args, **kwargs)
    

class Login(LoginView):
    template_name = 'base.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')



class Registro(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(Registro, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user