from django.contrib import admin
from . import models


class PointOfInterestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['title', 'category', 'description', 'address']}),
        ('Localisation',    {'fields': ['is_localised', 'date_localised',
                                        'addresse_localised', 'latitude',
                                        'longitude']}),
        ('Debug',           {'fields': ['geojson_response']}),
    ]
    readonly_fields = ["geojson_response", ]
    list_display = ('title', 'address', 'is_localised', 'category')
    list_filter = ['is_localised', 'date_localised', 'category']
    search_fields = ['title', 'description', 'address', 'addresse_localised']

admin.site.register(models.PointOfInterest, PointOfInterestAdmin)


class POICategoryAdmin(admin.ModelAdmin):
    fields = ['label', 'color_id', 'description']
    list_display = ('label', 'color_id', 'description')
    search_fields = ['label', 'description']

admin.site.register(models.POICategory, POICategoryAdmin)