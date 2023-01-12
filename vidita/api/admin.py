from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User_Model, Picture_Model


admin.site.register(User_Model, UserAdmin)


class Picture_Admin(admin.ModelAdmin):
    list_display = ('date', 'location', 'description',
                    'uploaded_by', 'image')
    list_display_links = ('uploaded_by', 'image')
    search_fields = ('description', 'tagged_people')


admin.site.register(Picture_Model, Picture_Admin)