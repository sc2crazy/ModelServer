from django.db import models
from django.contrib.auth.models import User
from categories.models import Category, SubCategory
from assets.models import Asset


def upload_thumbnail_location(instance, filename):
    extension = filename.split(".")[-1]
    return "%s/%s/%s.%s" % (instance.asset.subcategory.category.name,
                            instance.asset.subcategory.name,
                            instance.asset.name,
                            extension)


class Descriptor(models.Model):
    asset = models.ForeignKey(Asset, related_name="descriptor", on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to=upload_thumbnail_location, null=True, blank=True)
    width = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    owner = models.ForeignKey(User, related_name="asset", on_delete=models.DO_NOTHING)
    isPrivate = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    fork = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s in %s" % (self.asset.name, self.asset.subcategory.name)
