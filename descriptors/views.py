from rest_framework import generics
from .models import Descriptor
from .serializers import DescriptorSerializer


class DescriptorList(generics.ListCreateAPIView):
    queryset = Descriptor.objects.all()
    serializer_class = DescriptorSerializer


class DescriptorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Descriptor.objects.all()
    serializer_class = DescriptorSerializer
