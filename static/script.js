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

    // Array to hold existing values
    var existingValues = ["Suite Room", "Family Room", "Deluxe Room", "Classic Room", "Superior Room", "Luxury Room"];

    $('#data-form').submit(function(event) {
        event.preventDefault(); // Prevent form submission

        var inputValue = $('#roomtype').val().trim();

        // Check if the input value already exists in the array
        if (existingValues.includes(inputValue)) {
            alert("Value must be unique!");
        } else {
            // If value is unique, do something here (like submitting the form)
            alert("Value is unique! Submitting form...");
            // Uncomment the line below to actually submit the form
            // $(this).unbind('submit').submit();
        }
    });
});
