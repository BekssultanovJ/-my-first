from django.shortcuts import render

import product
from product.models import Product


def products_list(request):
    products = Product.objects.all()
    context = {'products': product}
    return render(request, 'prodact/products_list.html', context)

