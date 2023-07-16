from django.core.mail import send_mail
from config import settings


def send_new_password(email, new_password):
    send_mail(
        subject='Ваш пароль был изменен',
        message=f'Ваш новый пароль для авторизации в личном кабинете {new_password}.\n'
                f'После смены пароля вам необходимо заново авторизоваться.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
