from django.urls import path

from .views import Apply

app_name = "promotions"

urlpatterns = [
    path("", Apply.as_view(), name="apply"),
]
