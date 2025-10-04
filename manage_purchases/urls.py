from django.urls import path

from .views import PurchaseIndex, PurchaseDetail

app_name = "manage_purchases"

urlpatterns = [
    path("", PurchaseIndex.as_view(), name="index"),
    path("<int:pk>/", PurchaseDetail.as_view(), name="detail"),
]
