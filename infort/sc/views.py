from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from .models import *
from .forms import AddschematicForm, VendorForm, AddOrderForm, RegisterUserForm
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'sc/home.html', {'title': 'Главная страница'})


class SchematicView(ListView):
    model = Schematic
    template_name = 'sc/schematic.html'
    context_object_name = 'schematics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendor'] = Vendor.objects.all()
        return context


class ServicesView(ListView):
    paginate_by = 10
    model = Service
    template_name = 'sc/service.html'
    context_object_name = 'services'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stages'] = Stage.objects.all()
        return context

    def get_queryset(self):
        if 'stage_slug' in self.kwargs:
            return Service.objects.filter(stage__slug=self.kwargs['stage_slug'])
        return Service.objects.all()


class OrderView(DetailView):
    model = Service
    context_object_name = 'order'
    template_name = 'sc/order.html'

    def get_queryset(self):
        return Service.objects.filter(pk=self.kwargs.get('pk'))
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class AddOrderView(CreateView):
    form_class = AddOrderForm
    template_name = 'sc/addorder.html'
    success_url = reverse_lazy('service')


def schema(request, result):
    vendor = Vendor.objects.all()
    schematic = Schematic.objects.filter(manufactured__vendor=result)
    return render(request, 'sc/schematic.html', {'title': 'Схемы', 'vendor': vendor, 'schematics': schematic})


def addschema(request):
    if request.method == 'POST':
        form = AddschematicForm(request.POST, request.FILES)
        if form.is_valid():
            Schematic.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = AddschematicForm()
    return render(request, 'sc/addschema.html', {'title': 'Добавить схему', 'form': form})


def addvendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            Vendor.objects.create(**form.cleaned_data)

    else:
        form = AddschematicForm()
    return render(request, 'sc/addschema.html', {'title': 'Добавить схему', 'form': form})


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'sc/register.html'
    success_url = reverse_lazy('login')


class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'sc/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

