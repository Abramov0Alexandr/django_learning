from django.views import generic
from catalog.models import Product
from catalog.services import get_category_cache


class IndexListView(generic.ListView):
    queryset = Product.objects.all()
    cats = get_category_cache()
    template_name = 'catalog/index.html'
    extra_context = {'cats': cats,
                     'cat_selected': 0}


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'
