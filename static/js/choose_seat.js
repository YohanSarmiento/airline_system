var ticketElement = document.getElementById('ticket-info');
var ticketId = ticketElement.dataset.ticketId;

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

$(document).ready(function () {
    // Función para actualizar la información del asiento seleccionado
    function updateSelectedSeatInfo(seatNumber, seatType, seatPrice) {
        // Actualiza el div con la información del asiento seleccionado
        $('.num_seat').text(seatNumber);
        $('.type_seat').text(seatType);
        $('.total_price div:last-child').text(`COP ${seatPrice}`);
    }

    // Al hacer clic en un asiento
    $('.div-wrapper').click(function () {
        // Remueve la clase de selección de todos los asientos
        $('.div-wrapper').removeClass('selected');

        // Agrega la clase de selección al asiento clickeado
        $(this).addClass('selected');

        // Obtiene la información del asiento seleccionado
        var seatNumber = $('.div-wrapper.selected .text-wrapper').text();
        var seatType = getSeatType(seatNumber);  // Obtén el tipo de asiento

        // Puedes ajustar el precio según el tipo de asiento
        var seatPrice = calculateSeatPrice(seatType);  // Puedes ajustar esto según tu lógica

        // Actualiza la información del asiento seleccionado
        updateSelectedSeatInfo(seatNumber, seatType, seatPrice);
    });

    // Al hacer clic en el botón de aceptar
    $('#btn-aceptar').click(function () {
        // Obtiene el número de asiento y el ID del ticket seleccionado
        var seatNumber = $('.div-wrapper.selected .text-wrapper').text();
        // var ticketId = '{{ ticket.id }}';  // Asegúrate de incluir el ID del ticket
        console.log(ticketId);
        const csrfToken = getCookie('csrftoken');

        // Envía una solicitud al servidor para actualizar el ticket con el asiento
        fetch('/flights/update_ticket/' + ticketId + '/add_seat/' + seatNumber + '/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Asegúrate de incluir el token CSRF si es necesario
            },
            body: JSON.stringify({}),
        })
        .then(response => response.json())
        .then(data => {
            window.location.href = '/flights/flight_fare/' + data.ticket_id;
        })
        .catch(error => console.error('Error:', error));
    });

    // Función para obtener el tipo de asiento (ventana, pasillo o centro)
    function getSeatType(seatNumber) {
        var seatLetter = seatNumber.charAt(seatNumber.length - 1).toUpperCase();

        if (seatLetter === 'A' || seatLetter === 'F') {
            return 'Ventana';
        } else if (seatLetter === 'B' || seatLetter === 'E') {
            return 'Centro';
        } else if (seatLetter === 'C' || seatLetter === 'D') {
            return 'Pasillo';
        } else {
            return 'Desconocido';
        }
    }

    // Función para calcular el precio del asiento según el tipo (puedes ajustar esto según tu lógica)
    function calculateSeatPrice(seatType) {
        // Puedes definir diferentes precios según el tipo de asiento
        if (seatType === 'Ventana') {
            return 40000;
        } else if (seatType === 'Centro') {
            return 35000;
        } else if (seatType === 'Pasillo') {
            return 38000;
        } else {
            return 0;  // Valor predeterminado si el tipo de asiento es desconocido
        }
    }
});