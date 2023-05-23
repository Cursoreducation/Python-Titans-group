from django.urls import path
from .views import main, add_to_cart, cart, checkout, checkout_proceed

urlpatterns = [
    path("", main),
    path("add-to-cart/<int:product_id>", add_to_cart, name="add_to_cart"),
    path("cart", cart, name="cart"),
    path("checkout", checkout, name="checkout"),
    path("checkout/procceed", checkout_proceed, name="checkout_proceed"),
]
