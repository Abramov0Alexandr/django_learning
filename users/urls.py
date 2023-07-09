from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from users.views import RegistrationView, ProfileView, ConfirmView, gen_password


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),

    path('registration/', RegistrationView.as_view(), name='registration'),
    path('verify/<key>/', ConfirmView.as_view(), name='confirm'),
    path('registration/notification/',
         TemplateView.as_view(template_name='users/reg_notification.html'), name='notification'),
    path('reg-success/', TemplateView.as_view(template_name='users/reg_success.html'), name='reg_success'),

    path('profile/', ProfileView.as_view(), name='profile_edit'),
    path('profile/gen-password', gen_password, name='gen_password')
]

