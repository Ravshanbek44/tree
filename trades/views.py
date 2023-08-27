from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
# from rest_framework.response import Response
# from rest_framework.views import APIView
# import pandas as pd
from .models import Region, District, TreeClassifier, TypeTree, TreeDeliveryCompany, Trade
from .serializers import RegionSerializer, DistrictSerializer, TreeTypeSerializer, TreeClassifierSerializer, \
    TreeDeliveryCompanySerializer, TradeSerializer


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DistrictListAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = District.objects.all()
        pk = self.request.GET.get('region_id')
        if pk:
            queryset = queryset.filter(region_id=pk)
        return queryset


class TreeClassifierListAPIView(generics.ListAPIView):
    queryset = TreeClassifier.objects.all()
    serializer_class = TreeClassifierSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class TypeTreeListAPIView(generics.ListAPIView):
    serializer_class = TreeTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = TypeTree.objects.all()
        pk = self.request.GET.get('classifier_id')
        if pk:
            queryset = queryset.filter(classifier_id=pk)
        return queryset


class TreeDeliveryListAPIView(generics.ListAPIView):
    serializer_class = TreeDeliveryCompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = TreeDeliveryCompany.objects.all()
        pk = self.request.GET.get('region_id')
        if pk:
            queryset = queryset.filter(address_id=pk)
        return queryset


class TradeCreateAPIView(generics.CreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]