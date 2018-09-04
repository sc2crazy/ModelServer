from django.db import models
from categories.models import Category, SubCategory


def upload_asset_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s/%s" % (instance.subcategory.category.name, instance.subcategory.name, instance.name)


class Asset(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategory, related_name="asset", on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=upload_asset_location)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
