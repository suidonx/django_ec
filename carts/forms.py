from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label="",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
