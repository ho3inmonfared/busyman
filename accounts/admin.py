from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models, forms


@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):

    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser

    ordering = ("phone",)

    list_display = (
        "phone",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "is_staff",
        "is_active",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone",
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    search_fields = (
        "phone",
        "first_name",
        "last_name",
    )