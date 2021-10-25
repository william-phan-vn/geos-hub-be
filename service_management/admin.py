from django.contrib import admin
from service_management.models import Service, OsPlatform, ServicePrice


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')


admin.site.register(ServicePrice, ServiceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OsPlatform, ServiceAdmin)
