from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Item


# Create your views here.
class Index(ListView):
    template_name = "manage_items/index.html"
    model = Item
