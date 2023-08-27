from django.contrib import admin
from config import settings
from .models import TreeClassifier, TypeTree, Region, District, TreeDeliveryCompany, Trade


class TreeClassifierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TreeTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'classifier']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']


class TreeDeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']


class TradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'contract_number']

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )


admin.site.register(TreeClassifier, TreeClassifierAdmin)
admin.site.register(TypeTree, TreeTypeAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(TreeDeliveryCompany, TreeDeliveryAdmin)
admin.site.register(Trade, TradeAdmin)
