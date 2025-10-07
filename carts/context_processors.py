from .models import CartItem

from checkouts.forms import BillingAddressForm


# ユーザーのカート情報、請求先入力フォーム、カート内アイテムの合計金額をテンプレート共通のコンテキスト化
def item_in_cart(request):
    item_in_cart = (
        CartItem.objects.all()
        .filter(session=request.session.session_key)
        .prefetch_related("item")
    )

    form = BillingAddressForm()

    purchase_amount = sum([cart_item.calc_total_amount for cart_item in item_in_cart])

    # Promotion Codeが適用されている場合は割引
    discount = request.session.get("discount", None)
    if discount:
        purchase_amount = max(purchase_amount - discount, 0)

    return {
        "item_in_cart": item_in_cart,
        "purchase_amount": purchase_amount,
        "form": form,
    }
