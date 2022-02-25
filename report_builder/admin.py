from django.contrib import admin
from .models import (Report,
                     Equipment,
                     Clients,
                     OutageType,
                     Cause,
                     Comment)

admin.site.register(Report)
admin.site.register(Equipment)
admin.site.register(Clients)
admin.site.register(OutageType)
admin.site.register(Cause)
admin.site.register(Comment)
