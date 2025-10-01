from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class PurchaseHistory(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BillingAddress(models.Model):
    COUNTRY_CHOICES = [
        ("", "選択してください"),
        ("Japan", "日本"),
    ]
    STATE_CHOICES = [
        ("", "選択してください"),
        ("Tokyo", "東京"),
    ]
    purchased_id = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)
    first_name = models.CharField()
    last_name = models.CharField()
    user_name = models.CharField()
    email = models.EmailField()
    address = models.CharField()
    address2 = models.CharField(null=True, blank=True)
    country = models.CharField(choices=COUNTRY_CHOICES)
    state = models.CharField(choices=STATE_CHOICES)
    zip = models.CharField(validators=[RegexValidator(r"\d{7}")])
    name_on_card = models.CharField()
    credit_card_number = models.CharField(validators=[RegexValidator(r"\d{14}")])
    expiration = models.DateField()
    cvv = models.CharField(validators=[RegexValidator(r"\d{3}")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    purchased_id = models.ForeignKey(PurchaseHistory, on_delete=models.CASCADE)
    name = models.CharField()
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
