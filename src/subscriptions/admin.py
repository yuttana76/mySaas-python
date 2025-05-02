from django.contrib import admin

# Register your models here.
from .models import Subscription, UserSubscription, SubscriptionPrice

# class SubscriptionPrice(admin.StackedInline): # Show in  more detail
class SubscriptionPrice(admin.TabularInline):  #Show in line
    model = SubscriptionPrice
    readonly_fields = ['stripe_id']
    # can_delete = False
    extra = 0

class SubscriptionAdmin(admin.ModelAdmin):
    inlines = [SubscriptionPrice]
    list_display = ['name', 'active', 'stripe_id']
    # readonly_fields = ['stripe_id']
    

admin.site.register(Subscription,SubscriptionAdmin)


admin.site.register(UserSubscription)