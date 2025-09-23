from django.shortcuts import render
from django.views.generic.list import ListView

from items.models import Item


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
