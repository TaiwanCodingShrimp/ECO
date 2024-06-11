from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import FootPrint, User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "title", "phone", "location", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("title", "phone", "location")}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "title",
                    "phone",
                    "location",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


class FootPrintAdmin(admin.ModelAdmin):
    readonly_fields = ("carbon_footprint",)
    list_display = ("users_id", "distance", "method", "carbon_footprint", "date")
    fields = ("users_id", "distance", "method", "carbon_footprint", "date")
    list_filter = ("users_id", "method", "date")
    search_fields = ("users_id__username", "method")

    def save_model(self, request, obj, form, change):
        obj.update_carbon_footprint()
        super().save_model(request, obj, form, change)


admin.site.register(FootPrint, FootPrintAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
