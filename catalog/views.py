from django.urls import reverse_lazy
from django.views import generic
from catalog.forms import CreateProductForm
from catalog.models import Product


class IndexListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'catalog/index.html'
    extra_context = {'title': 'SkyStore', }


class ProductDetailView(generic.DetailView):

    model = Product
    template_name = 'catalog/product_detail.html'
    slug_url_kwarg = 'product_slug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['product_slug'])


class ContactsView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class CreateProductCreateView(generic.CreateView):

    form_class = CreateProductForm
    template_name = 'catalog/create_product.html'

    def get_success_url(self):
        return reverse_lazy('catalog:homepage')


class EditProductUpdateView(generic.UpdateView):

    form_class = CreateProductForm
    template_name = 'catalog/create_product.html'
    slug_url_kwarg = 'product_slug'

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['product_slug'])

    def get_success_url(self):
        return reverse_lazy('catalog:homepage')
