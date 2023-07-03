from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from users.models import User


class RegistrationView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/registration.html'
