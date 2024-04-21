$(document).ready(function () {
    // Function to prompt alert for user's name
    function promptUserName() {
        var userName = prompt("Please enter your name mentioned in your booking", "");
        var currentUrl = window.location.href;

        // Create a URL object
        var urlObject = new URL(currentUrl);

        // Get the pathname from the URL object
        var pathname = urlObject.pathname;

        // Check if the pathname is valid and not empty
        if (pathname && pathname !== '/') {
            // Split the pathname by '/' and extract the last part, which is the token
            var token = pathname.split('/').pop();
        }
        if (userName != null && userName != "") {
            // Send the username to Flask for validation
            $.ajax({
                type: "POST",
                url: "/validate-username",
                data: { username: userName, token: token },
                success: function (response) {
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


