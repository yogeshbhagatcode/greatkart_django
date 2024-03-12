from .views import _create_cart
from .models import Cart, CartItem


def cart_item_counter(request):
    cart_product_count = 0

    try:
        cart_id = _create_cart(request)
        cart_items = CartItem.objects.filter(cart__cart_id=cart_id)
        
        for cart_item in cart_items:
            cart_product_count += cart_item.quantity
    except:
        pass

    return dict(cart_product_count=cart_product_count)
