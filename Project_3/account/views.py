from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from .forms import UserAccountRegistrationForms, UserAccountProfileForm
from .models import ProUser

class CreateUserAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForms

    def get_success_url(self):
        return reverse('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


def success_func(request):
    return render(request=request,
                  template_name='success.html')


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Login as a user'}
    # success_url = reverse_lazy('success')

    def get_success_url(self):
        return reverse('success')


class UserAccountLogoutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Logout from LMS'}


class UserAccountUpdateView(UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Edit current user'}
    form_class = UserAccountProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('success')

class LeaderBoard(ListView):
    model = ProUser
    template_name = 'leaderboard.html'
    context_object_name = 'players_list'
    paginate_by = 20
