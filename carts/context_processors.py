from .models import CartItem


# ユーザーのカート情報をテンプレート共通のコンテキスト化
def item_in_cart(request):
    item_in_cart = (
        CartItem.objects.all()
        .filter(session=request.session.session_key)
        .prefetch_related("item")
    )

    purchase_amount = sum([cart_item.calc_total_amount for cart_item in item_in_cart])

    return {
        "item_in_cart": item_in_cart,
        "purchase_amount": purchase_amount,
    }
