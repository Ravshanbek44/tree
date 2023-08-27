from rest_framework import serializers
from .models import TreeDeliveryCompany, TreeClassifier, TypeTree, District, Region, Trade


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'region']


class TreeClassifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeClassifier
        fields = ['id', 'name']


class TreeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTree
        fields = ['id', 'name', 'classifier']


class TreeDeliveryCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeDeliveryCompany
        fields = ['id', 'address', 'name']


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = [
            'id',
            'status',
            'type_tree',
            'count_tree',
            'district',
            'latitude',
            'longitude',
            'contract_number',
            'contract_date',
            'contract_file',
            'delivery_company',
            'created_at',
        ]


class TradeSerializerReport(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = [
            'id',
            'status',
            'contract_number',
            'contract_date',
            'created_at'
        ]
