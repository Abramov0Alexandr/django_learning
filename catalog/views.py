from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse, reverse_lazy
from django.views import generic
from catalog.forms import CreateProductForm, VersionForm
from catalog.models import Product, Version


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


class ProductCreateView(LoginRequiredMixin, generic.CreateView):

    form_class = CreateProductForm
    template_name = 'catalog/create_product.html'

    def get_success_url(self):
        product = self.object
        return reverse('catalog:product_info', args=[product.slug])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)

        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        self.object.product_owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):

    form_class = CreateProductForm
    template_name = 'catalog/create_product.html'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)

        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['product_slug'])

    def get_success_url(self):
        return reverse('catalog:edit_product', args=[self.kwargs.get('product_slug')])


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'catalog/confirm_delete_product.html'
    slug_url_kwarg = 'product_slug'
    success_url = reverse_lazy('catalog:homepage')

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs['product_slug'])
