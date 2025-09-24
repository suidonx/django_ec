from django.urls import path

from . import views

app_name = "manage_items"

urlpatterns = [
    path("items/", views.Index.as_view(), name="index"),
    path("items/create/", views.CreateItem.as_view(), name="create"),
    path("items/update/<int:pk>", views.UpdateItem.as_view(), name="update"),
    path("items/delete/<int:pk>", views.DeleteItem.as_view(), name="delete"),
]
