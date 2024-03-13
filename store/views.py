from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from cart.models import Cart, CartItem
from cart.views import _create_cart
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True).order_by('id')
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page_number')
    paged_products = paginator.get_page(page_number)
    product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render (request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_create_cart(request), product=product).exists()
    except Exception as e:
        raise e
    context = {
        'product': product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword)).order_by('-created_date')
        product_count = products.count()
        context = {
        'products': products,
        'product_count': product_count,
    }
    return render (request, 'store/store.html', context)