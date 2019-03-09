from django.contrib import admin
from .models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['title', 'description', 'address']}),
        ('Localisation',    {'fields': ['is_localised', 'date_localised',
                                        'addresse_localised', 'latitude',
                                        'longitude']}),
        ('Debug',           {'fields': ['geojson_response']}),
    ]
    readonly_fields = ["geojson_response", ]
    list_display = ('title', 'address', 'is_localised')
    list_filter = ['is_localised', 'date_localised']
    search_fields = ['title', 'description', 'address', 'addresse_localised']


admin.site.register(PointOfInterest, PointOfInterestAdmin)
