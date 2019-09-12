from django.contrib import admin
from .models import Photo
# Register your models here.
class Photo_admin(admin.ModelAdmin):
    list_display = ['title', 'upload_time',]

    class Meta:
        model = Photo
admin.site.register(Photo, Photo_admin)