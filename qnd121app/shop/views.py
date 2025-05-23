from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .recommender import Recommender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def cart_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/cart_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    product = get_object_or_404(Product,
                                id=id,
                                available=True)
    if category_slug:
        category = get_object_or_404(Category,category_slug=category_slug)
        products = products.filter(category=category)

    cart_product_form = CartAddProductForm()

    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                  'category': category,
                  'cart_product_form': cart_product_form,
                  'recommended_products': recommended_products,
                  'products': products})
