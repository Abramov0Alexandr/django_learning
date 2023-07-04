from django.urls import reverse_lazy
from django.views import generic
from users.forms import UserRegistrationForm, ProfileEditForm
from users.models import User


class RegistrationView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')


class ProfileView(generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    success_url = reverse_lazy('users:profile_edit')
    template_name = 'users/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user

