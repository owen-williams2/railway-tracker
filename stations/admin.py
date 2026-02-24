from django.contrib import admin
from .models import Station, RailTrip, Amendment

admin.site.register(Station)
admin.site.register(RailTrip)
admin.site.register(Amendment)