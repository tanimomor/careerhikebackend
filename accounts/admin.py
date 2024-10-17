from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'phone_number', 'user_type', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'user_type')

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password')}),
        ('Personal info', {'fields': ('user_type',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'phone_number', 'password1', 'password2', 'user_type', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )

    search_fields = ('email', 'phone_number')
    ordering = ('email', 'phone_number')
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
