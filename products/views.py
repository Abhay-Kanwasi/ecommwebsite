from django.shortcuts import render, redirect
from products.models import Product, SizeVariant

from accounts.models import Profile

def get_product(request , slug):
    
    # print(request.user.profile.get_cart_count)
    print(Profile.profile_image)
    # profile, created = Profile.objects.get_or_create(user=request.user)
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

