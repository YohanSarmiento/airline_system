var ticketElement = document.getElementById('ticket-info');
var ticketId = ticketElement.dataset.ticketId;

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function elegirOpcion(option) {
    // var ticketId = '{{ ticket.id }}';
    const csrfToken = getCookie('csrftoken');
    fetch('/flights/update_ticket_fare/' + ticketId + '/' + option + '/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken // Asegúrate de incluir el token CSRF si es necesario
        },
        body: JSON.stringify({}),
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = '/flights/user_data_form/' + data.ticket_id;
    })
    .catch(error => console.error('Error:', error))
}
