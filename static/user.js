$(document).ready(function() {
    $('#startdate').on('change', function() {
        var startDate = new Date($(this).val());
        $('#enddate').attr('min', $(this).val()); // Set min date for end date
        $('#enddate').val($(this).val()); // Automatically set end date to start date
    });
});
