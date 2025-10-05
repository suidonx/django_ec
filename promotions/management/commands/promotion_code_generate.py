from random import randint
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string

from promotions.models import PromotionCode


class Command(BaseCommand):
    help = "10個のプロモーションコードを生成します。"

    def handle(self, *args, **options):
        num = 10
        digit = 7
        min_value = 100
        max_value = 1000

        if PromotionCode.objects.count() == num:
            print(f"すでに{num}個のプロモーションコードが登録されています。")

        else:
            PromotionCode.objects.bulk_create(
                [
                    PromotionCode(
                        code=get_random_string(digit),
                        discount_amount=randint(min_value, max_value),
                    )
                    for _ in range(num)
                ]
            )

            print(f"{num}個のプロモーションコードを生成しました。")

        # 共通処理
        print("-----生成されたプロモーションコード-----")
        for promo_code in PromotionCode.objects.all():
            print(promo_code.code)
