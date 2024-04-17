$(document).ready(function() {
    $('#startdate').on('change', function() {
        var startDate = new Date($(this).val());
        var minEndDate = new Date(startDate.getTime() + (24 * 60 * 60 * 1000)); // Add 1 day to start date
        $('#enddate').attr('min', minEndDate.toISOString().split('T')[0]); // Set min date for end date
    });

    // Prevent user from selecting previous dates for start date
    var today = new Date().toISOString().split('T')[0];
    $('#startdate').attr('min', today);
});
