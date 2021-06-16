from django.contrib import admin
from .models import (Report,
                     Services,
                     #  ServiceAmount,
                     Clients,
                     #  ClientAmount,
                     OutageType,
                     Cause)

admin.site.register(Report)
admin.site.register(Services)
# admin.site.register(ServiceAmount)
admin.site.register(Clients)
# admin.site.register(ClientAmount)
admin.site.register(OutageType)
admin.site.register(Cause)
