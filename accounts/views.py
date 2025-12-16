from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class LoginView(LoginView):
    template_name = 'accounts/login.html'


class LogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')