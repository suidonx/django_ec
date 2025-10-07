from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import View

from carts.models import CartItem
from .models import PromotionCode


# Create your views here.
class Apply(View):
    def get(self, request, *args, **kwargs):
        return redirect("items:index")

    def post(self, request):
        input_value = request.POST["promotion_code"]
        cart_items = CartItem.objects.filter(session=request.session.session_key)

        # カート内にアイテムが存在するかどうか
        if cart_items:
            try:
                # 該当するPromotion Codeがある場合、処理を継続する。ない場合、例外処理をする
                matched_code = PromotionCode.objects.get(code=input_value)

                # プロモーションコードがすでに使われているかどうか
                if matched_code.applied_at:
                    apply_error = "すでにそのプロモーションコードは使われています。"
                    return render(
                        request,
                        "carts/index.html",
                        {
                            "apply_error": apply_error,
                        },
                    )

                discount = matched_code.discount_amount

                # Promotion Code情報をsessionに記憶させる
                request.session["applied"] = True
                request.session["discount"] = discount
                request.session["promotion_code"] = input_value

                return render(
                    request,
                    "carts/index.html",
                )

            # 該当するPromotion Codeがなければエラーメッセージを返す
            except ObjectDoesNotExist:
                apply_error = "プロモーションコードが間違っています。"
                return render(
                    request,
                    "carts/index.html",
                    {
                        "apply_error": apply_error,
                    },
                )
        # カート内にアイテムが存在しない
        else:
            apply_error = "カート内にアイテムがありません。"
            return render(
                request,
                "carts/index.html",
                {
                    "apply_error": apply_error,
                },
            )
