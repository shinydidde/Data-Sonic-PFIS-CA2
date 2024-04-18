$(document).ready(function () {
    // Get the start and end dates from the form
    let startDate = sessionStorage.getItem('startDate');
    let endDate = sessionStorage.getItem('endDate');
    $("#bookNow").click(function (e) {
        e.preventDefault();
        let params = new window.URLSearchParams(window.location.search);
        let id = params.get('id')
        window.location.href = $(this).attr("href") + '?id=' + id + '&startDate=' + encodeURIComponent(startDate) + '&endDate=' + encodeURIComponent(endDate);;;
    });

    $("#check_in").val(startDate);
    $("#check_out").val(endDate);

    var roomSelect = document.getElementById('room_type');
    let availability = $(this).data('availability');
    var addRoomButton = document.getElementById('addRoom');
    var deleteRoomButton = document.getElementById('deleteRoom');

    // Populate the select dropdown with room types
    function populateRoomOptions() {
        roomSelect.innerHTML = '';
        for (var room in availability) {
            var option = document.createElement('option');
            option.value = room;
            option.textContent = room + ' - ';
            if (availability[room] > 0) {
                option.textContent += 'Available';
            } else if (availability[room] == 0) {
                option.textContent += 'Fully Booked';
            } else {
                option.textContent += 'Not Available';
            }
            roomSelect.appendChild(option);
        }
    }

    // Function to add a new room
    addRoomButton.addEventListener('click', function() {
        var newRoom = prompt('Enter the new room type:');
        if (newRoom && !availability.hasOwnProperty(newRoom)) {
            availability[newRoom] = 1;
            populateRoomOptions();
        }
    });

    // Function to delete a room
    deleteRoomButton.addEventListener('click', function() {
        var selectedRoom = roomSelect.value;
        if (selectedRoom && confirm('Are you sure you want to delete ' + selectedRoom + '?')) {
            delete availability[selectedRoom];
            populateRoomOptions();
        }
    });

});
