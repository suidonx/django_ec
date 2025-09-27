from django.urls import path

from . import views

app_name = "carts"

urlpatterns = [
    path("", views.IndexCart.as_view(), name="index"),
    path("add/<int:pk>", views.AddToCart.as_view(), name="add"),
]
