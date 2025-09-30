from django.contrib.sessions.models import Session
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic import ListView, DeleteView

from .models import CartItem
from .forms import AddToCartForm
from items.models import Item


# Create your views here.
class IndexCart(ListView):
    template_name = "carts/index.html"
    model = CartItem


class AddToCart(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse("items:index"))

    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)

        # ユーザー特定のため
        request.session.save()
        session = Session.objects.get(session_key=request.session.session_key)

        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data["quantity"]

            item_in_cart, created = CartItem.objects.get_or_create(
                item=item,
                session=session,
                defaults={
                    "item": item,
                    "session": session,
                    "unit_price": item.price,
                    "quantity": quantity,
                },
            )

            if not created:
                item_in_cart.quantity += quantity
            item_in_cart.save()

            return redirect("carts:index")

        else:
            return redirect("items:index")


class DeleteCartItem(DeleteView):
    template_name = "carts/delete.html"
    model = CartItem
    success_url = reverse_lazy("carts:index")
