
from django.db.models.query_utils import Q
from django.shortcuts import render, resolve_url

from parts import forms
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
import json
from parts.models import Product
from django.contrib.auth.models import User

def order_create(request):
    
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.userid = request.user
            order.save()
            
            
            
            
                
                
                

            for key, value in request.session['cart'].items():
                prod = Product.objects.all()
                query = value['name']
                product_id = Product.objects.filter(name__icontains=query).first()
                

               
                OrderItem.objects.create(order=order,product=product_id,price =value['price'],quantity=value['quantity'],)
                    
                    
                    
                    
                    
            
            
            cart = Cart(request)
            cart.clear()
            
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})