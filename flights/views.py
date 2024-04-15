from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.http import JsonResponse
from .models import *
from django.template import loader
from .forms import FlightSearchForm, UserRegisterForm
from .utils import populate_seats
import random
import string

# Create your views here.

def home(request):
    form = FlightSearchForm()  # Create a new instance of the form
    return render(request, 'home.html', {'form': form})  # Pass it to the template


def select_fly(request):
    if request.method == 'POST':
        form = FlightSearchForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            origin = form.cleaned_data['origin']
            destination = form.cleaned_data['destination']
            # depart_date = form.cleaned_data['depart_date']
            # arrival_time = form.cleaned_data['arrival_time']
            flights = Flight.objects.filter(
                origin__city=origin,
                destination__city=destination,
                # depart_date=depart_date
            )
            return render(request, 'select_fly.html', {'flights': flights})

    else:
        form = FlightSearchForm()

    return render(request, 'home.html', {'form': form})

# def flight(request, flight_id):
#     flight = Flight.objects.get(pk=flight_id)
#     return render(request, "flight.html", {
#         "flight":flight,
#         "passengers": flight.passengers.all(),
#         "non_passengers": Passenger.objects.exclude(flights=flight).all()
#     })

def generate_ref_no():
    # Genera un código único de 6 caracteres
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def create_ticket(request, flight_id):
    # Obtén el vuelo
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        try:
            # Crea el ticket con el vuelo seleccionado
            ticket = Ticket.objects.create(flight=flight, ref_no=generate_ref_no())
            return JsonResponse({'ticket_id': ticket.id})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    # Devuelve un error si la solicitud no es POST
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def choose_seat(request, ticket_id):
    # Obtén el ticket
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Renderiza la página de selección de asientos con el ticket
    return render(request, 'choose_seat.html', {'ticket': ticket})


def update_ticket_add_seat(request, ticket_id, seat_number):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    try:
        # Attempt to get the existing seat
        seat = Seat.objects.get(seat_number=seat_number, is_reserved=True)
    except Seat.DoesNotExist:
        # If the seat doesn't exist, create a new one
        plane_id = ticket.flight.plane.id  # Assuming plane is a ForeignKey in Seat
        seat = Seat.objects.create(seat_number=seat_number, is_reserved=True, plane_id=plane_id)

    # Assign the seat to the ticket
    ticket.seat = seat
    ticket.save()

    return JsonResponse({'ticket_id': ticket.id})




def flight_fare(request, ticket_id):
    # Obtén el ticket
    ticket = get_object_or_404(Ticket, id=ticket_id)
    try:
        if(len(Ticket.objects.all()) > 1):
            latest_ticket = Ticket.objects.all().order_by('-created_at')[1]
        else:
            latest_ticket = None
    except Ticket.DoesNotExist:
        latest_ticket = None
    
    if latest_ticket:
        last_fare = latest_ticket.fare
        return render(request, 'flight_fare.html', {'ticket': ticket, 'last_fare': last_fare})
    else:
        return render(request, 'flight_fare.html', {'ticket': ticket})

def update_ticket_fare(request, ticket_id, option):
    try:
        ticket = get_object_or_404(Ticket, id=ticket_id)
        ticket.fare = option
        ticket.save()
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'ticket_id': ticket.id})

try:
    planes = Plane.objects.all()

    if planes.exists():
        # Extract registration numbers for all planes
        registration_numbers = planes.values_list('registration_number', flat=True)
        
        # Populate seats for each plane
        for registration_number in registration_numbers:
            populate_seats([registration_number])
            
    else:
        print("No planes found.")

except Exception as e:
    print(f"Error: {e}")

def user_data_form(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'user_data_form.html', {'ticket':ticket,'form': UserRegisterForm})

def registro_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    form = UserRegisterForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['nombres']
        last_name = form.cleaned_data['apellidos']
        email = form.cleaned_data['correo']
        flights = [ticket.flight]
        passenger = Passenger.objects.create(first_name=first_name, last_name=last_name)
        passenger.flights.set(flights)
        passenger.save()

        passengers = [passenger]
        ticket.passenger.set(passengers)
        ticket.email = email
        ticket.save()

    return render(request, 'payment.html', {'ticket_id': ticket_id})

def my_flights(request):
    tickets = Ticket.objects.all()
    return render(request, 'my_flights.html', {'tickets': tickets})