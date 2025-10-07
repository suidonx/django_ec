from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from carts.models import CartItem
from promotions.models import PromotionCode
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

                # Promotion Codeを使用している場合
                if request.session.get("applied", False):
                    promotion_code = PromotionCode.objects.get(
                        code=request.session["promotion_code"]
                    )
                    # 現在時間を記録し、適用した事実を記録
                    promotion_code.applied_at = timezone.now()
                    promotion_code.save()

                    # 購入履歴とプロモーションコードを紐づける
                    purchase_history.promotion_code = promotion_code
                    purchase_history.save()

                # 請求住所フォームを受け取りDBに保存する
                billing_address = form.save(commit=False)
                billing_address.purchased_id = purchase_history
                billing_address.save()

                # カート商品を注文商品DBに保存する
                for cart_item in cart_items:
                    OrderItem.objects.create(
                        purchased_id=purchase_history,
                        name=cart_item.item.name,
                        unit_price=cart_item.unit_price,
                        quantity=cart_item.quantity,
                    )

                # メッセージ機能
                messages.success(request, "購入ありがとうございます")

                # 注文合計金額を計算
                purchase_amount = sum(
                    [cart_item.calc_total_amount for cart_item in cart_items]
                )
                # promotion codeが使われた時、割引処理
                discount = request.session.get("discount", None)
                if discount:
                    purchase_amount = max(purchase_amount - discount, 0)

                # メール送信機能
                send_mail(
                    subject="購入明細",
                    message=render_to_string(
                        "checkouts/purchase_notification_mail.txt",
                        {
                            "cart_items": cart_items,
                            "purchase_amount": purchase_amount,
                            "discount": discount,
                            "promotion_code": request.session.get(
                                "promotion_code", None
                            ),
                        },
                    ),
                    from_email=None,
                    recipient_list=[billing_address.email],
                )

                # カート情報、プロモーションコード情報をリセット
                request.session.flush()
                return redirect("items:index")

            # フォームのバリデーションエラー
            else:
                return render(request, "carts/index.html", context={"form": form})

        # カート内に商品がないとき
        else:
            messages.error(request, "カートに商品がありません")
            return render(request, "carts/index.html", context={"form": form})
