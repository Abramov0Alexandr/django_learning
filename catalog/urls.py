from django.urls import path
from catalog.views import homepage, contact


urlpatterns = [
    path('', homepage),
    path('contacts/', contact, name='contact')
]
