from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from orders.models import Order, OrderItem


class OrderItemInlineAdmin(admin.StackedInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_contact_person",
        "wallet",
        "pickup_time",
        "outlet",
        "comment",
    )
    search_fields = ("order_contact_person", "wallet")
    inlines = [OrderItemInlineAdmin]


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
