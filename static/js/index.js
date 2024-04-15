document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#flight-from").addEventListener("input", event => {
        flight_from(event);
    });

    // document.querySelector("#flight-to").addEventListener("input", event => {
    //     flight_to(event);
    // });

    document.querySelector("#flight-from").addEventListener("focus", event => {
        flight_from(event, true);
    });

    // document.querySelector("#flight-to").addEventListener("focus", event => {
    //     flight_to(event, true);
    // });

    // document.querySelectorAll('.trip-type').forEach(type => {
    //     type.onclick = trip_type;
    // });

});

function showplaces(input) {
    let box = input.parentElement.querySelector(".places_box");
    box.style.display = 'block';
}

function hideplaces(input) {
    let box = input.parentElement.querySelector(".places_box");
    setTimeout(() => {
        box.style.display = 'none';
    }, 300);
}

function selectplace(option) {
    let input = option.parentElement.parentElement.querySelector('input[type=text]');
    input.value = option.dataset.value.toUpperCase();
    input.dataset.value = option.dataset.value;
}

function flight_from(event, focus=false) {
    let input = event.target;
    let list = document.querySelector('#places_from');
    showplaces(input);
    if(!focus) {
        input.dataset.value = '';
    }
    if(input.value.length > 0) {
        fetch('query/places/'+input.value)
        .then(response => response.json())
        .then(places => {
            list.innerHTML = '';
            places.forEach(element => {
                let div = document.createElement('div');
                div.setAttribute('class', 'each_places_from_list');
                div.classList.add('places__list');
                div.setAttribute('onclick', "selectplace(this)");
                div.setAttribute('data-value', element.code);
                div.innerText = `${element.city}`;
                list.append(div);
            });
        });
    }
}