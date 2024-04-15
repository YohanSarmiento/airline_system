function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


document.addEventListener('DOMContentLoaded', function () {
    // var csrfToken = document.body.getAttribute('data-csrf');
    const csrfToken = getCookie('csrftoken');

    // Obtén todas las tarjetas de vuelo
    var flightCards = document.querySelectorAll('.container');

    // Agrega un evento de clic a cada tarjeta de vuelo
    flightCards.forEach(function (card) {
        card.addEventListener('click', function () {
            // Obtiene el ID del vuelo desde la tarjeta
            var flightId = card.id.split('-')[1];

            fetch('/flights/create_ticket/' + flightId + '/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({}),
            })
            .then(response => response.json())
            .then(data => {
                window.location.href = '/flights/choose_seat/' + data.ticket_id;
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

