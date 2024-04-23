$(document).ready(function () {
    // $(".update-booking").click(function () {
    //     $("#token").val(token);
    //     $("#type").val('edit');
    //     $("#manage-booking-form").submit();
    // });

    $(".delete-booking").click(function () {
        var token = $(this).data('token');
        $.ajax({
            type: "POST",
            url: "/admin/dashboard/bookings",
            data: { token: token, type:'delete' },
            success: function (response) {
                if (response) {
                    console.log(response);
                } else {
                    console.log("Invalid");
                }
            }
        });
    });

});


