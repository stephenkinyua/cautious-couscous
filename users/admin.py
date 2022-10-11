from django.contrib import admin
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """
    Define admin model for custom User model with no email field.
    """

    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    list_display_links = ("phone_number", 'first_name')
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "id",
        "phone_number",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    )
    search_fields = (
        "phone_number",
        "first_name",
        "last_name",
    )
    ordering = ("phone_number",)
    list_per_page = 25

