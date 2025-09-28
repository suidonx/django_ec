from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "value": 1}),
    )
