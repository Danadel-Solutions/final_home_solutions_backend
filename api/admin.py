from django.contrib import admin
from .models import Property


# class PhotoBookInline(admin.TabularInline):
#     model = PhotoBook


# class PropertyAdmin(admin.ModelAdmin):
#     inlines = [
#         PhotoBookInline,
#     ]


admin.site.register(Property)
# admin.site.register(PhotoBook)

# Register your models here.
