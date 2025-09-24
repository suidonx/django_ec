from django.forms import ModelForm

from items.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "item_code", "price", "content", "image"]
