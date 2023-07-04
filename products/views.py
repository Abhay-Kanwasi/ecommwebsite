from django.shortcuts import render, redirect
from products.models import Product

from accounts.models import Cart, CartItems
from django.http import HttpResponseRedirect
def get_product(request , slug):
    try:
        product = Product.objects.get(slug = slug)
        context = {'product' : product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            print(price) #price according to size
        return render(request , 'product/product.html', context = context)
    
    except Exception as e:
        print(e)

def add_to_cart(request, slug):
    variant = request.GET.get('variant')
    if variant:
        variant = request.GET.get('variant')
    product = Product.objects.get(slug= slug)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user = user, is_paid = False)
    return HttpResponseRedirect(request.path_info)
