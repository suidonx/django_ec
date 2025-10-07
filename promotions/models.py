from django.db import models


# Create your models here.
class PromotionCode(models.Model):
    code = models.CharField(unique=True)
    discount_amount = models.PositiveIntegerField()
    applied_at = models.DateTimeField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
