$(document).ready(function () {
    // Prompt user for their name
    var userName = prompt("Please validate your name (It should be same as it was in the booking):");
    // Send an AJAX request to the server to validate the name
    var xhr = new XMLHttpRequest();
     // Get the token from the URL
     var url = window.location.href;
     var token = url.split('/').pop();
     xhr.open("POST", "/manage-booking/" + token);
    xhr.setRequestHeader("Content-Type", "application/json"); // Set correct Content-Type header
    xhr.send(JSON.stringify({ name: userName }));
    xhr.onload = function () {
        if (xhr.status === 200) {
            // If the name is valid, redirect to the main page
            window.location.href = "/main";
        } else {
            // If the name is invalid, display an error message
            alert("Invalid name. Please try again.");
            // Reload the page to prompt for name again
            window.location.reload();
        }
    };


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
