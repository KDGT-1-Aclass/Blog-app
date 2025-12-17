from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


class AccountLoginView(LoginView):
    template_name = 'registration/login.html'


class LogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')