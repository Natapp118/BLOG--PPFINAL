from django.urls import path, include
from django.contrib.auth.views import LogoutView
from MYAPP import views
from .views import login_view, Registro
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import Registro

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

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('inicio/', views.inicio, name="inicio"),
    path('programacion/', views.programacion, name="programacion"),
    path('Ingenieria', views.Ingenieria, name="Ingenieria"),
    path("Contacto/", views.Contacto, name="Contacto"),
    path('formulario', views.formulario, name="formulario"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', login_view, name='login'),
    path('Registro',views.Registro, name="Registro"),
    path('about/', views.about, name='about'),
]