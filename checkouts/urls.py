from django.urls import path

from . import views

app_name = "checkouts"

urlpatterns = [
    path("", views.CheckOut.as_view(), name="checkouts"),
]
