from django.shortcuts import render
from django.views.generic import ListView

from .models import CartItem


# Create your views here.
class IndexCart(ListView):
    template_name = "carts/index.html"
    model = CartItem
