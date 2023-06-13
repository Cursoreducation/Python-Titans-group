from django.contrib import admin
from .models import MenuItem, SliderItem, OrderItem, Order, RefferalLink

admin.site.register(MenuItem)
admin.site.register(SliderItem)
admin.site.register(RefferalLink)


class OrderItemInline(admin.StackedInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = fields = ['first_name', "last_name", "address", "email"]
    inlines = [
        OrderItemInline
    ]


admin.site.register(Order, OrderAdmin)