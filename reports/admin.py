from django.conf import settings
from django.contrib import admin
from .models import TreeReport


# class VenueAdmin(admin.TabularInline):
#     list_display = ('report', 'latitude', 'longitude',)
#     search_fields = ('report',)
#
#     fieldsets = (
#         (None, {
#             'fields': ('report', 'latitude', 'longitude',)
#         }),
#     )
#
#     class Media:
#         if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
#             css = {
#                 'all': ('css/admin/location_picker.css',),
#             }
#             js = (
#                 'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
#                 'js/admin/location_picker.js',
#             )


class TreeReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'company_stir']

    # fieldsets = (
    #     (None, {
    #         'fields': ('report', 'latitude', 'longitude',)
    #     }),
    # )

    class Media:
        if hasattr(settings, 'GOOGLE_MAPS_API_KEY') and settings.GOOGLE_MAPS_API_KEY:
            css = {
                'all': ('css/admin/location_picker.css',),
            }
            js = (
                'https://maps.googleapis.com/maps/api/js?key={}'.format(settings.GOOGLE_MAPS_API_KEY),
                'js/admin/location_picker.js',
            )


admin.site.register(TreeReport, TreeReportAdmin)
