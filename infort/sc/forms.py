from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddschematicForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddschematicForm, self).__init__(*args, **kwargs)
        self.fields['manufactured'].empty_label = 'Производитель не выбран'

    class Meta:
        model = Schematic
        fields = '__all__'


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


class AddOrderForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(AddOrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Service
        fields = ['clients', 'devices', 'manufactured', 'model', 'serial', 'bug', 'stage']
        widgets = {
            'clients': forms.Select(attrs={'class': 'form-select'}),
            'devices': forms.Select(attrs={'class': 'form-select'}),
            'manufactured': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'bug': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'stage': forms.Select(attrs={'class': 'form-select'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    pass
