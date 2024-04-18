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

    let availability = JSON.parse($(this).data('availability'));
    let roomSelect = document.getElementById('room_type');

    // Function to add a new room
    document.getElementById('addRoom').addEventListener('click', function() {
        let newRoom = prompt('Enter the new room type:');
        if (newRoom) {
            availability[newRoom] = 1;
            updateRoomOptions();
        }
    });

    // Function to delete a room
    document.getElementById('deleteRoom').addEventListener('click', function() {
        var selectedRoom = roomSelect.value;
        if (selectedRoom && confirm('Are you sure you want to delete ' + selectedRoom + '?')) {
            delete availability[selectedRoom];
            updateRoomOptions();
        }
    });

    // Function to update the room select options
    function updateRoomOptions() {
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

});
