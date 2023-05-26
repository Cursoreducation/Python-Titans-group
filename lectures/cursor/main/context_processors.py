from .models import MenuItem
from products.models import Category

def menu(request):
    return {
        "menu_items": MenuItem.objects.all(),
        "categories": Category.objects.filter(parent_id=None),
        "cart_length": len(request.session.get("cart", []))
    }