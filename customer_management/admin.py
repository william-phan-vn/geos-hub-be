from django.contrib import admin

from customer_management.models import Customer, PaidCustomer


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(PaidCustomer, CustomerAdmin)
