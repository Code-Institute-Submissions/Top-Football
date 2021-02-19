from django.contrib import admin
from .models import OrderInformation, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):

    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_costs', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email_address', 'contact_number',
              'street_name_1', 'street_name_2', 'county',
              'postal_code', 'delivery_costs', 'order_total',
              'grand_total')

    list_display = ('order_number', 'date', 'full_name',
                    'delivery_costs', 'order_total',
                    'grand_total')

    ordering = ('-date',)


admin.site.register(OrderInformation, OrderAdmin)
