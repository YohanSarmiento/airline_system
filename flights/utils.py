from flights.models import *
from .models import Plane, Seat


from flights.models import *
from .models import Plane, Seat

def populate_seats(registration_numbers):
    try:
        for registration_number in registration_numbers:
            print(f"Processing registration number: {registration_number}")
            plane = Plane.objects.get(registration_number=registration_number)
            plane_capacity = plane.capacity  # Access the plane's capacity field

            # Calculate the number of seats per row based on capacity and desired configuration
            seats_per_row = 6  # Adjust this value based on your seat configuration (e.g., 3x3, 4x3)
            num_rows = plane_capacity // seats_per_row  # Integer division for full rows
            remaining_seats = plane_capacity % seats_per_row  # Seats remaining for the last row

            for row in range(1, num_rows + 1):
                for seat_letter in ['a', 'b', 'c', 'd', 'e', 'f']:
                    seat_number = f"{row}{seat_letter}"

                    # Check if the seat already exists for the current plane
                    if not Seat.objects.filter(plane=plane, seat_number=seat_number).exists():
                        print(f"Creating seat: {seat_number} for plane: {registration_number}")
                        Seat.objects.create(plane=plane, seat_number=seat_number)

            # Handle remaining seats in the last row (if any)
            if remaining_seats > 0:
                for seat_letter in range(ord('a'), ord('a') + remaining_seats):
                    seat_number = f"{num_rows}{chr(seat_letter)}"
                    if not Seat.objects.filter(plane=plane, seat_number=seat_number).exists():
                        print(f"Creating seat: {seat_number} for plane: {registration_number}")
                        Seat.objects.create(plane=plane, seat_number=seat_number)

    except Plane.DoesNotExist:
        print(f"Plane with registration number {registration_number} does not exist.")


# def populate_seats(registration_numbers):
#     try:
#         for registration_number in registration_numbers:
#             print(f"Processing registration number: {registration_number}")
#             plane = Plane.objects.get(registration_number=registration_number)
#             seat_rows = 25  # Assuming you have 25 rows

#             for row in range(1, seat_rows + 1):
#                 for seat_letter in ['a', 'b', 'c', 'd', 'e', 'f']:
#                     seat_number = f"{row}{seat_letter}"

#                     # Check if the seat already exists for the current plane
#                     if not Seat.objects.filter(plane=plane, seat_number=seat_number).exists():
#                         print(f"Creating seat: {seat_number} for plane: {registration_number}")
#                         Seat.objects.create(plane=plane, seat_number=seat_number)

#     except Plane.DoesNotExist:
#         print(f"Plane with registration number {registration_number} does not exist.")




