from django.contrib import admin

# Register your models here.
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "stripe_id")
    search_fields = ("user__username", "stripe_id")
    list_filter = ("user__is_active",)
    ordering = ("user__username",)
# admin.site.register(Customer)