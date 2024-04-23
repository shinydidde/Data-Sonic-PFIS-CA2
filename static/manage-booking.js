$(document).ready(function () {

    var userName = prompt("Please enter your name mentioned in your booking", "");
    var currentUrl = window.location.href;
    var urlObject = new URL(currentUrl);
    var pathname = urlObject.pathname;
    let token
    if (pathname && pathname !== '/') {
        token = pathname.split('/').pop();
    }

    // Function to prompt alert for user's name
    function promptUserName() {

        if (userName != null && userName != "") {
            $.ajax({
                type: "POST",
                url: "/manage-booking/"+token,
                data: { username: userName, token: token, type:'check' },
                success: function (response) {
                    if (response.valid) {
                        $(".change-title").text('Edit Booking');
                        var name = response.name;
                        var price = response.price;
                        var email = response.email;
                        var room_type = response.room_type;
                        var check_in = response.check_in;
                        var check_out = response.check_out;
                        var note = response.note;

                        $("#name").val(name);
                        $("#email").val(email);
                        $("#price").val(price);
                        $("#room_type").append($('<option>', {
                            value: room_type,
                            text: room_type
                        }));
                        $("#check_in").val(check_in);
                        $("#check_out").val(check_out);
                        $("#note").val(note);
                        $("#type").val('edit');
                        $("#manage-booking-form").show();
                    } else {
                        alert("Invalid username. Please try again.");
                    }
                }
            });
        }
    }

    // $(".update-booking").click(function () {
    //     $("#token").val(token);
    //     $("#type").val('edit');
    //     $("#manage-booking-form").submit();
    // });

    $(".delete-booking").click(function () {
        $.ajax({
            type: "POST",
            url: "/admin/dashboard/bookings",
            data: { token: token, type:'delete' },
            success: function (response) {
                if (response.valid) {
                    alert(response);
                } else {
                    alert("Invalid");
                }
            }
        });
    });

    // Execute the promptUserName function when the page loads
    promptUserName();

});


