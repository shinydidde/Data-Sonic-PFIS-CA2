$(document).ready(function () {
    // Prompt user for name
    var name = prompt("Please validate your name (It should be same as it was in the booking):");
    // Get the token from the URL
    var url = window.location.href;
    var token = url.split('/').pop();
    // Send name to Flask backend
    fetch('/manage-booking/' +token, {
        method: 'POST',
        body: JSON.stringify({ name: name }),
        headers:{
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Redirect user or handle response data
        if (data.valid) {
            // Redirect to dashboard
            window.location.href = '/dashboard';
        } else {
            alert("Invalid name. Please try again.");
        }
    });


    $(".update-booking").click(function () {
        $(".change-title").text('Edit Booking');
        $("#roomtype").attr('readonly', 'readonly');
        var roomtype = $(this).data('roomtype');
        var occupancy = $(this).data('occupancy');
        var roomprice = $(this).data('roomprice');
        var available = $(this).data('available');
        var roomimage = $(this).data('roomimage');
        var roomtitle = $(this).data('roomtitle');
        var roomdesc = $(this).data('roomdesc');

        $("#roomtype").val(roomtype);
        $("#occupancy").val(occupancy);
        $("#roomprice").val(roomprice);
        $("#available").val(available);
        $("#roomimage").val(roomimage);
        $("#roomtitle").val(roomtitle);
        $("#roomdesc").val(roomdesc);
        $("#type").val('update');
        $("#data-form").show();
    });

    // $(".delete-booking").click(function () {
    //     var roomtype = $(this).data('roomtype');
    //     $("#roomtype").val(roomtype);
    //     $("#type").val('remove');
    //     $("#data-form").submit();
    // });

});
