from django.contrib import admin
from .models import ImageUploadModel


# Register your models here.
class Image_Uploead_Admin(admin.ModelAdmin):
    list_display = ('description', 'document',) #list_display의 변수명은 고정


admin.site.register(ImageUploadModel,Image_Uploead_Admin)
