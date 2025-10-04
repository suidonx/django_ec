from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator

from basicauth.decorators import basic_auth_required

from checkouts.models import OrderItem, PurchaseHistory


# Create your views here.
@method_decorator(basic_auth_required, name="dispatch")
class PurchaseIndex(ListView):
    template_name = "manage_purchases/index.html"
    model = PurchaseHistory


@method_decorator(basic_auth_required, name="dispatch")
class PurchaseDetail(View):
    def get(self, request, pk):
        purchase_history = PurchaseHistory.objects.get(id=pk)
        order_item = OrderItem.objects.filter(purchased_id=purchase_history)

        purchase_amount = sum([item.calc_total_amount for item in order_item])
        sum_count = order_item.aggregate(sum_count=Sum("quantity"))["sum_count"]

        return render(
            request,
            "manage_purchases/detail.html",
            {
                "order_item": order_item,
                "purchase_amount": purchase_amount,
                "sum_count": sum_count,
            },
        )
