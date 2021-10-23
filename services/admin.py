from django.contrib import admin
from services.models import Service, OsPlatform, ServicePrice


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time',)


admin.site.register(ServicePrice, ServiceAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OsPlatform, ServiceAdmin)
