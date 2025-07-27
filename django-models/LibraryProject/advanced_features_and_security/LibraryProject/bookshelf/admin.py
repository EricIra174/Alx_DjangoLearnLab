from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExampleModel, CustomUser

# Register ExampleModel
admin.site.register(ExampleModel)

# Custom admin for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register CustomUser with the custom admin
"admin.site.register(CustomUser, CustomUserAdmin)"
