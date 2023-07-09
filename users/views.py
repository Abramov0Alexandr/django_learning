from random import randint
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from config import settings
from users.forms import UserRegistrationForm, ProfileEditForm
from users.models import User


class RegistrationView(generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:notification')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_key = ''.join([str(randint(0, 9))
                                                for _ in range(21)])

        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Для завершения регистрации, пожалуйста, перейдите по указанной ссылке '
                    f'http://127.0.0.1:8000/auth/verify/{self.object.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ConfirmView(generic.TemplateView):

    def get(self, *args, **kwargs):
        key = self.kwargs.get('key')
        user = User.objects.filter(verification_key=key).first()
        if user:
            user.is_active = True
            user.verification_key = key
            user.save()
            login(self.request, user)
        return redirect('users:reg_success')


class ProfileView(generic.UpdateView):
    model = User
    form_class = ProfileEditForm
    success_url = reverse_lazy('users:profile_edit')
    template_name = 'users/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user


def gen_password(request):
    new_password = ''.join([str(randint(0, 9)) for _ in range(9)])
    send_mail(
        subject='Ваш пароль был изменен',
        message=f'Ваш новый пароль для авторизации в личном кабинете {new_password}.\n'
                f'После смены пароля вам необходимо заново авторизоваться.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))

