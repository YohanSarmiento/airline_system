from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('select_fly/', select_fly, name='select_fly'),
    path('create_ticket/<int:flight_id>/', create_ticket, name='create_ticket'),
    path('choose_seat/<int:ticket_id>/', choose_seat, name='choose_seat'),
    path('update_ticket/<int:ticket_id>/add_seat/<str:seat_number>/', update_ticket_add_seat, name='actualizar_ticket_add_seat'),
    path('flight_fare/<int:ticket_id>/',flight_fare , name='select_fare'),
    path('update_ticket_fare/<int:ticket_id>/<str:option>/',update_ticket_fare, name="update_ticket_fare"),
    path('user_data_form/<int:ticket_id>', user_data_form, name="user_data_form"),
    path('user_payment_form/<int:ticket_id>', registro_view, name="user_payment_form"),
    path('my_flights', my_flights, name="my_flights")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
