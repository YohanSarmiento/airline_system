from django.contrib import admin

from .models import Flight, Airport, Passenger, Ticket, Plane, Seat
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin","depart_date","depart_time","destination","arrival_date","arrival_time", "duration", "plane","get_plane_name")

    def get_plane_name(self, obj):
        return obj.plane.name if obj.plane else None

    get_plane_name.short_description = 'Plane Name'

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

class PlaneAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "capacity", "registration_number")

class SeatAdmin(admin.ModelAdmin):
    list_display = ("id", "seat_number", "is_reserved", "plane")

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Ticket)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(Seat, SeatAdmin)
