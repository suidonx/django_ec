from django.contrib.sessions.models import Session
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .models import CartItem
from items.models import Item


# Create your views here.
class IndexCart(ListView):
    template_name = "carts/index.html"
    model = CartItem


class AddToCart(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse("items:index"))

    def post(self, request, pk):
        item = Item.objects.get(id=pk)
        request.session.setdefault("item_in_cart", True)
        session = Session.objects.get(session_key=request.session.session_key)

        try:
            item_in_cart = CartItem.objects.get(session=session, item=item)
            item_in_cart.quantity += 1
            item_in_cart.save()

        except CartItem.DoesNotExist:
            CartItem.objects.create(
                session=session,
                item=item,
                unit_price=item.price,
                quantity=1,
            )
            return redirect(reverse("items:index"))
        else:
            return redirect(reverse("items:index"))
