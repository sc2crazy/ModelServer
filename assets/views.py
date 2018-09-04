from rest_framework import generics
from .models import Asset
from .serializers import AssetSerializer


class AssetList(generics.ListCreateAPIView):
    """
    List all the assets Or Create a new one when POST
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET, PUT, PATCH, DELETE a single specified asset
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
