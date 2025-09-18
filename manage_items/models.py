from django.db import models
from django.apps import apps

# Create your models here.
Item = apps.get_model("items.Item")
