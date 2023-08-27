from django.contrib import admin
from .models import News, ForUsers


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class ForUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(News, NewsAdmin)
admin.site.register(ForUsers, ForUserAdmin)
