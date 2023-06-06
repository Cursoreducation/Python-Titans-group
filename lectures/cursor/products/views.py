from django.shortcuts import render, redirect
from .models import Category, Product, Comment


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, "category.html", {"category": category, "products": category.products.all()})


def product_page(request, slug):
    product = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(parent_id=None).filter(product_id=product.id)
    return render(request, "product.html", {"product": product, "images": product.images.all(), "comments": comments})


def add_comment(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        if request.method == "POST":
            comment = Comment()
            comment.user = request.user
            comment.product_id = product_id
            comment.text = request.POST.get("comment-text")
            if request.POST.get("parent", False):
                comment.parent_id = int(request.POST.get("parent"))
            comment.save()
            return redirect("/products/" + product.slug)
    return redirect("/")