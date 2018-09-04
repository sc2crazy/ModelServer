from rest_framework import serializers
from .models import Descriptor


class DescriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptor
        exclude = ["isPrivate", ]
