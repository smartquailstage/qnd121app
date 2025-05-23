from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

app_name = 'shop'

urlpatterns = [
    path('lista/', views.product_list, name='product_list'),
    path('cart_list/', views.cart_list, name='cart_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]