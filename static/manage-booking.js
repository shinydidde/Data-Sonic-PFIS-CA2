$(document).ready(function () {
    // Function to prompt alert for user's name
    function promptUserName() {
        var userName = prompt("Please enter your name mentioned in your booking", "");
        var currentUrl = window.location.href;
        var urlObject = new URL(currentUrl);
        var pathname = urlObject.pathname;
        if (pathname && pathname !== '/') {
            var token = pathname.split('/').pop();
        }
        if (userName != null && userName != "") {
            $.ajax({
                type: "POST",
                url: "/validate-username",
                data: { username: userName, token: token },
                success: function (response) {
                    // Handle the response from Flask
                    if (response.valid) {
                            $(".change-title").text('Edit Booking');
                            var name = response.name;
                            var email = $(this).data('occupancy');
                            var room_type = $(this).data('room_type');
                            var check_in = $(this).data('check_in');
                            var check_out = $(this).data('check_out');
                            var note = $(this).data('roomtitle');

                            $("#name").val(name);
                            $("#email").val(email);
                            $("#room_type").val(room_type);
                            $("#check_in").val(check_in);
                            $("#check_out").val(check_out);
                            $("#note").val(note);
                            $("#roomdesc").val(roomdesc);
                            $("#type").val('edit');
                            $("#manage-booking-form").show();
                    } else {
                        alert("Invalid username. Please try again.");
                    }
                }
            });
        }
    }

    // Execute the promptUserName function when the page loads
    promptUserName();

    $(".update-booking").click(function () {
        $("#manage-booking-form").submit();
    });

    $(".delete-booking").click(function () {
        $("#token").val($(this).data('token'));
        $("#type").val('delete');
        $("#data-form").submit();
    });

});


