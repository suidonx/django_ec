from django.urls import path

from . import views

app_name = "manage_items"

urlpatterns = [
    path("items/", views.Index.as_view(), name="index"),
]
