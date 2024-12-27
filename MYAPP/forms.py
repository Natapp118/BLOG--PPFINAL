from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm

class Ingenieriaformulario(forms.Form):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    email = forms.EmailField()

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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