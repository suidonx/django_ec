from django.db import models
from django.contrib.sessions.models import Session

from items.models import Item


# Create your models here.
class CartItem(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    unit_price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(quantity__gte=0), name="quantity_gte_0"
            ),
            models.CheckConstraint(
                check=models.Q(unit_price__gt=0), name="unit_price_gt_0"
            ),
        ]
