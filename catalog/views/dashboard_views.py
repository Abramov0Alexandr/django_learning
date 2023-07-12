from django.views import generic
from catalog.models import Product


class IndexListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'catalog/index.html'
    extra_context = {'title': 'SkyStore', }


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'
