from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    item_code = models.CharField(max_length=30, default="SID-dddd")
    price = models.IntegerField()
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=0), name="price_gt_0"),
        ]
