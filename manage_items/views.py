from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic import CreateView

from items.models import Item
from .forms import ItemForm


# Create your views here.
class Index(ListView):
    template_name = "manage_items/index.html"
    model = Item

    # コンテキストを追加
    def get_context_data(self, **kwargs):
        # フィールド名の一覧を取得
        fields = Item._meta.get_fields()
        fields_names = [v.name for v in fields]

        # 各レコードの属性値を取得
        items = Item.objects.all()
        attrs = []
        for item in items:
            attr = []
            for field in fields_names:
                attr.append(getattr(item, field))
            attrs.append(attr)

        context = super().get_context_data(**kwargs)
        extra_context = {
            "fields_names": fields_names,
            "attrs": attrs,
        }
        context.update(extra_context)
        return context


class CreateItem(CreateView):
    success_url = reverse_lazy("manage_items:index")
    form_class = ItemForm
    template_name = "manage_items/create.html"
