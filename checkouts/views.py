from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from carts.models import CartItem
from .forms import BillingAddressForm
from .models import PurchaseHistory, OrderItem


# Create your views here.
class CheckOut(View):
    def get(self, request):
        return redirect("items:index")

    def post(self, request):
        form = BillingAddressForm(request.POST)
        cart_items = CartItem.objects.filter(
            session=request.session.session_key
        ).prefetch_related("item")

        # カート内に商品が存在するかどうか
        if cart_items.exists():
            # フォームのバリデーションチェック
            if form.is_valid():
                purchase_history = PurchaseHistory.objects.create()

                billing_address = form.save(commit=False)
                billing_address.purchased_id = purchase_history
                billing_address.save()

                for cart_item in cart_items:
                    OrderItem.objects.create(
                        purchased_id=purchase_history,
                        name=cart_item.item.name,
                        unit_price=cart_item.unit_price,
                        quantity=cart_item.quantity,
                    )

                messages.success(request, "購入ありがとうございます")

                purchase_amount = sum(
                    [cart_item.calc_total_amount for cart_item in cart_items]
                )
                send_mail(
                    subject="購入明細",
                    message=render_to_string(
                        "checkouts/purchase_notification_mail.txt",
                        {
                            "cart_items": cart_items,
                            "purchase_amount": purchase_amount,
                        },
                    ),
                    from_email=None,
                    recipient_list=[billing_address.email],
                )

                return redirect("items:index")

            # フォームのバリデーションエラー
            else:
                return render(request, "carts/index.html", context={"form": form})

        # カート内に商品がないとき
        else:
            messages.error(request, "カートに商品がありません")
            return render(request, "carts/index.html", context={"form": form})
