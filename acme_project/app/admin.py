from django.contrib import admin
from .models import Driver, Constructor, Circuit, Event, Result

admin.site.register(Driver)
admin.site.register(Constructor)
admin.site.register(Circuit)
admin.site.register(Event)
admin.site.register(Result)
