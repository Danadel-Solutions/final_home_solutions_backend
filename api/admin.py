from django.contrib import admin
from .models import Property, PhotoBook

class PhotoBookInline(admin.TabularInline):
    model = PhotoBook
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PhotoBookInline,]

admin.site.register(Property, PropertyAdmin)
admin.site.register(PhotoBook)

# Register your models here.
