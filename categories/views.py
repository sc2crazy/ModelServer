from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer
from assets.models import Asset
from assets.serializers import AssetSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CategoryDetailView(APIView):
    def get_objects(self, pk):
        try:
            return SubCategory.objects.filter(category=pk)
        except SubCategory.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        subs = self.get_objects(pk)
        serializer = SubCategorySerializer(subs, many=True)
        return Response(serializer.data)


class SubCategoryDetailView(APIView):
    def get_objects(self, pk):
        try:
            return Asset.objects.filter(subcategory=pk)
        except Asset.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        assets = self.get_objects(pk)
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)
