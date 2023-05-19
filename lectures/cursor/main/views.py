from django.shortcuts import render
from .models import MenuItem
from products.models import Product, Category


def main(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(show_on_main_page=True)
    categories = Category.objects.filter(parent_id=None)
    return render(request, "index.html", {"menu_items": menu_items, "products": products, "categories": categories})