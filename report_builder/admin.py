from django.contrib import admin
from .models import (Report,
                     Services,
                     Clients,
                     OutageType,
                     Cause,
                     Comment)

admin.site.register(Report)
admin.site.register(Services)
admin.site.register(Clients)
admin.site.register(OutageType)
admin.site.register(Cause)
admin.site.register(Comment)
