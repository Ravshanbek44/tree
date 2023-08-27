from rest_framework import serializers
from .models import Contract, ContractWithPartner


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'status',
            'number_contract',
            'date_contract',
            'number_akt',
            'date_akt',
            'company_stir',
            'name_company',
            'owner_jshshir',
            'owner_fio',
            'phone',
            'number_report',
            'description',
            'created_at',
            'image',
            'image1',
            'image2',
            'image3',
        ]


class ContractSerializerReport(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'number_contract',
            'date_contract',
            'name_company',
            'created_at'
            'status',
        ]


class ContractWithPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractWithPartner
        fields = [
            'id',
            'status',
            'number_contract',
            'date_contract',
            'number_akt',
            'date_akt',
            'company_stir',
            'name_company',
            'owner_jshshir',
            'owner_fio',
            'partner_stir',
            'partner_name',
            'partner_owner_jshshir',
            'partner_fio',
            'description',
            'created_at'
        ]


class ContractWithPartnerSerializerReport(serializers.ModelSerializer):
    class Meta:
        model = ContractWithPartner
        fields = [
            'id',
            'status',
            'number_contract',
            'date_contract',
            'name_company',
            'partner_name',
            'created_at'
        ]
