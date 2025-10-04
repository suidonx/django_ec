from django import forms

from .models import BillingAddress


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = "__all__"
        exclude = ["purchased_id"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "first_name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "id": "last_name"}
            ),
            "user_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "user_name",
                    "placeholder": "Username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "you@example.com",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "address",
                }
            ),
            "address2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "address2",
                }
            ),
            "country": forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "country",
                }
            ),
            "state": forms.Select(
                attrs={
                    "class": "form-control",
                    "id": "state",
                }
            ),
            "zip": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "zip",
                    "placeholder": "1000014",
                }
            ),
            "name_on_card": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name_on_card",
                }
            ),
            "credit_card_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "credit_card_number",
                    "placeholder": "1234123412341234",
                }
            ),
            "expiration": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "expiration",
                    "placeholder": "MM/YY",
                    "maxlength": 5,
                },
            ),
            "cvv": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "cvv",
                    "placeholder": "CVV",
                }
            ),
        }
