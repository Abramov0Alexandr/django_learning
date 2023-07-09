from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        is_active = False
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'password1', 'password2',)
        help_texts = {
            'patronymic': 'Данное поле опционально',
        }
        error_messages = {
            'email': {
                'unique': "Указанная электронная почта уже используется.",
            },
        }


class ProfileEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
