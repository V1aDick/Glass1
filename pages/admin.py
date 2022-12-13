from django.contrib import admin
from .models import CustomUser, Feedback, Record, Service
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Feedback)
admin.site.register(Record)
admin.site.register(Service)