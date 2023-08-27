from django.contrib import admin
from .models import Contract, ContractWithPartner


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_contract', 'number_akt']


class ContractWithPartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_contract', 'partner_name']


admin.site.register(Contract, ContractAdmin)
admin.site.register(ContractWithPartner, ContractWithPartnerAdmin)
