from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     def __str__(self):
#         return f"{self.id}: {self.first_name} {self.last_name}"
    
# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} {self.code}"

class Plane(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(help_text="Capacidad de pasajeros")
    registration_number = models.CharField(max_length=20, unique=True, help_text="Número de registro del avión")

    def __str__(self):
        return self.registration_number

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    depart_date = models.DateField(null=True)
    depart_time = models.TimeField(auto_now=False, auto_now_add=False)
    duration = models.IntegerField()
    arrival_date = models.DateField(null=True)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, to_field='registration_number')
    status_flight = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('departed', 'Departed'), ('arrived', 'Arrived'), ('canceled', 'Canceled')])  
    price = models.CharField(max_length=40, default="0")
    

    def __str__(self):
        return f"{self.id}: {self.depart_date} {self.depart_time} {self.origin} to {self.destination} {self.arrival_date}  {self.arrival_time} ({self.status_flight})"

class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.first_name}"

FARE_TYPE = (
    ('basic', 'Basic'),
    ('light', 'Light'),
    ('full', 'Full'),
    ('premium', 'Premium')
)

TICKET_STATUS =(
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('CANCELLED', 'Cancelled')
)


class Seat(models.Model):
    seat_number = models.CharField(max_length=10, unique=False, help_text="Número de asiento")  # Assuming a format like '1a', '2b', etc.
    is_reserved = models.BooleanField(default=False, help_text="¿El asiento está reservado?")
    # plane = models.ForeignKey(Plane, on_delete=models.CASCADE, related_name='seats', help_text="Avión al que pertenece el asiento")
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE, related_name='seats', help_text="Avión al que pertenece el asiento")

    def __str__(self):
        return f"{self.seat_number} {self.plane}({'Reserved' if self.is_reserved else 'Available'})"
    
class Ticket(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings", blank=True, null=True)
    ref_no = models.CharField(max_length=6, unique=True)
    passenger = models.ManyToManyField(Passenger, related_name="flight_tickets")
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE, blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets", blank=True, null=True)
    flight_destination_date = models.DateField(blank=True, null=True)
    flight_arrival_date = models.DateField(blank=True, null=True)
    flight_fare = models.FloatField(blank=True,null=True)
    total_fare = models.FloatField(blank=True, null=True)
    date_purchased = models.DateTimeField(auto_now_add=True)
    fare = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=45, blank=True)
    status = models.CharField(max_length=45, choices=TICKET_STATUS)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ref_no