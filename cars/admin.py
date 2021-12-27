from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:0px;" />'.format(object.car_photo.url))

    thumnail.short_description = 'Car Image'

    list_display = ('id', 'thumnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id',  'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmin)

