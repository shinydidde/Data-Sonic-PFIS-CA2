$(document).ready(function () {

     // Function to prompt alert for user's name
     function promptUserName() {
        var userName = prompt("Please enter your name mentioned in your booking", "");
        if (userName != null && userName != "") {
            // Send the username to Flask for validation
            $.ajax({
                type: "POST",
                url: "/validate-username",
                data: { username: userName },
                success: function(response) {
                    // Handle the response from Flask
                    if (response.valid) {
                        alert("Hello, " + userName + "! Welcome to our website!");
                    } else {
                        alert("Invalid username. Please try again.");
                    }
                }
            });
        }
        console.log(userName);
    }

    // Execute the promptUserName function when the page loads
    promptUserName();

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


