from django.views import generic
from catalog.models import Product, Category


class IndexListView(generic.ListView):
    queryset = Product.objects.all()
    cats = Category.objects.all()
    template_name = 'catalog/index.html'
    extra_context = {'cats': cats,
                     'cat_selected': 0}


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'
