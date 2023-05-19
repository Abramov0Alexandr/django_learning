from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'catalog/homepage.html')


def contact(request):
    return render(request, 'catalog/contacts.html')
