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

    //Booking Form
    $('#room_type').change(function() {
        availability = $(this).data('availability');
        var selectedRoomType = $(this).val();
        var availableRooms = parseInt(availability[selectedRoomType]);
        if (isNaN(availableRooms) || availableRooms < 0) {
            availableRooms = 0; // Treat negative values as zero
        }
        $('#room_number').attr('max', availableRooms); // Set max attribute of number input
        if (parseInt($('#room_number').val()) > availableRooms) {
            $('#room_number').val(availableRooms); // Reset value if it exceeds available rooms
        }
    });

});
