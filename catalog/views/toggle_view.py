from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from catalog.models import Product


class ToggleSalesStatusView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.set_sales_status'

    def get_object(self, queryset=None):
        product_slug = self.kwargs.get('product_slug')
        product = get_object_or_404(Product, slug=product_slug)

        if product.product_owner != self.request.user:
            raise Http404

        return product

    def get(self, request, product_slug):
        product = self.get_object()

        if product.in_stock:
            product.in_stock = False
        else:
            product.in_stock = True
        product.save()

        return redirect(reverse('catalog:homepage'))
