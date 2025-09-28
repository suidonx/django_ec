from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Item
from carts.forms import AddToCartForm


# Create your views here.
class Index(ListView):
    template_name = "items/index.html"
    model = Item


class Detail(DetailView):
    template_name = "items/detail.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_product"] = Item.objects.latest("id")

        form = AddToCartForm()
        context["form"] = form

        return context
