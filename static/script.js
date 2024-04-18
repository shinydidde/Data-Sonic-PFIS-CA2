$(document).ready(function () {
    $(".update-room").click(function () {
        $(".change-title").text('Edit Room');
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
    $(".delete-room").click(function () {
        var roomtype = $(this).data('roomtype');
        $("#roomtype").val(roomtype);
        $("#type").val('remove');
        $("#data-form").submit();
    });
    $(".add-room").click(function () {
        $(".change-title").text('Add Room');
        $("#roomtype").removeAttr('readonly');
        $('#data-form')[0].reset();
        $("#type").val('add');
    });

    $('.form-submit').click(function (event) {
        event.preventDefault(); // Prevent form submission
        var existingValues = $(this).data('roomtypes');
        if ($('#type').val() === 'add') {
            var inputValue = $('#roomtype').val().trim().toLowerCase();;
            // Check if the input value already exists in the array
            if (existingValues.map(function (val) { return val.toLowerCase(); }).includes(inputValue)) {
                alert("Room Type must be unique!");
            } else {
                $(this).unbind('submit').submit();
            }
        } else {
            $(this).unbind('submit').submit();
        }
    });
});
